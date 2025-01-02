from flask import Blueprint, render_template, request, redirect, url_for, session
from db import get_db_connection
from flask_bcrypt import Bcrypt
import DIETcalc
from utils import to_float
import json
import psycopg2
import psycopg2.extras
import logging


user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()


@user_bp.route('/profile', methods=['GET', 'POST'])
def profile():

    """
    Lietotāja profila funkcija.
    Apstrādā GET un POST pieprasījumus.
    - GET: Atgriež profila datu veidlapu.
    - POST: Apstrādā un saglabā lietotāja datus.
    """

    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cursor.execute("SELECT kategorija_key, nosaukums FROM kategorijas ORDER BY nosaukums")
        all_categories = [dict(row) for row in cursor.fetchall()]
        cursor.execute("SELECT * FROM produkts ORDER BY nosaukums")
        all_products = [dict(row) for row in cursor.fetchall()]

        if request.method == 'POST':
            name = request.form.get('name')
            surname = request.form.get('surname')
            email = request.form.get('email')
            password = request.form.get('password')
            age = int(request.form.get('age', 0))
            height = float(request.form.get('height', 0))
            weight = float(request.form.get('weight', 0))

            cursor.execute("SELECT min_limits, max_limits, selected_products FROM lietotajs WHERE id = %s", (session['user_id'],))
            existing_limits = cursor.fetchone()

            existing_min_limits = json.loads(existing_limits['min_limits']) if isinstance(existing_limits['min_limits'], str) else existing_limits['min_limits'] or {}
            existing_max_limits = json.loads(existing_limits['max_limits']) if isinstance(existing_limits['max_limits'], str) else existing_limits['max_limits'] or {}
            existing_selected_products = json.loads(existing_limits['selected_products']) if isinstance(existing_limits['selected_products'], str) else existing_limits['selected_products'] or []

            min_limits = json.loads(request.form.get('min_limits', '{}'))
            max_limits = json.loads(request.form.get('max_limits', '{}'))
            selected_products = json.loads(request.form.get('excluded_products', '[]'))

            for key, value in min_limits.items():
                if value is None:
                    existing_min_limits.pop(key, None)
                else:
                    existing_min_limits[key] = value

            for key, value in max_limits.items():
                if value is None:
                    existing_max_limits.pop(key, None)
                else:
                    existing_max_limits[key] = value

            hashed_password = None
            if password:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            cursor.execute("""
                UPDATE lietotajs
                SET vards = %s, uzvards = %s, epasts = %s, vecums = %s, augums = %s, svars = %s,
                    min_limits = %s, max_limits = %s, selected_products = %s
                    {password_clause}
                WHERE id = %s
            """.format(password_clause=", parole = %s" if hashed_password else ""),
            (
                name, surname, email, age, height, weight,
                json.dumps(existing_min_limits), json.dumps(existing_max_limits), json.dumps(selected_products),
                hashed_password, session['user_id']
            ) if hashed_password else (
                name, surname, email, age, height, weight,
                json.dumps(existing_min_limits), json.dumps(existing_max_limits), json.dumps(selected_products),
                session['user_id']
            ))
            connection.commit()

            return redirect(url_for('user_bp.profile'))

        cursor.execute("SELECT * FROM lietotajs WHERE id = %s", (session['user_id'],))
        user = dict(cursor.fetchone())

        user['min_limits'] = json.loads(user['min_limits']) if isinstance(user['min_limits'], str) else user['min_limits'] or {}
        user['max_limits'] = json.loads(user['max_limits']) if isinstance(user['max_limits'], str) else user['max_limits'] or {}
        user['selected_products'] = json.loads(user['selected_products']) if isinstance(user['selected_products'], str) else user['selected_products'] or []

        sorted_products = sorted(
            all_products,
            key=lambda x: (
                str(x['id']) not in user['selected_products'],
                not (str(x['id']) in user['min_limits'] or str(x['id']) in user['max_limits']),
                x['nosaukums'].lower()
            )
        )

        return render_template('profile.html', user=user, all_products=sorted_products, all_categories=all_categories)

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Database error occurred while processing your profile.")
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred.")

@user_bp.route('/calculate_menu', methods=['GET', 'POST'])
def calculate_menu():

    """
    Funkcija uztura plāna aprēķināšanai.
    Apstrādā GET un POST pieprasījumus.
    - GET: Iegūst lietotāja datus un parāda veidlapu veikalu izvēlei.
    - POST: Saglabā veikalu izvēli un aprēķina optimālo uztura plānu.
    """

    if 'user_id' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cursor.execute("SELECT * FROM lietotajs WHERE id = %s", (session['user_id'],))
        user = cursor.fetchone()

        if not user:
            return "User not found.", 404

        user_data = dict(user)

        user_data['min_limits'] = json.loads(user_data['min_limits']) if isinstance(user_data['min_limits'], str) else user_data['min_limits'] or {}
        user_data['max_limits'] = json.loads(user_data['max_limits']) if isinstance(user_data['max_limits'], str) else user_data['max_limits'] or {}
        user_data['selected_products'] = json.loads(user_data['selected_products']) if isinstance(user_data['selected_products'], str) else user_data['selected_products'] or []

        user_data['min_limits'] = {str(key): to_float(value) for key, value in user_data['min_limits'].items()}
        user_data['max_limits'] = {str(key): to_float(value) for key, value in user_data['max_limits'].items()}

        all_product_ids = set(user_data['selected_products']) | set(user_data['min_limits'].keys()) | set(user_data['max_limits'].keys())
        product_details = []

        for product_id in all_product_ids:
            cursor.execute("SELECT id, nosaukums FROM produkts WHERE id = %s", (product_id,))
            product = cursor.fetchone()
            if product:
                product_details.append({
                    'id': product['id'],
                    'name': product['nosaukums'],
                    'min_limit': user_data['min_limits'].get(str(product['id']), None),
                    'max_limit': user_data['max_limits'].get(str(product['id']), None),
                })

        user_data['selected_products'] = product_details

        error_message = None
        if request.method == 'POST':
            stores = []
            if request.form.get("store_maxima"):
                stores.append("Maxima")
            if request.form.get("store_rimi"):
                stores.append("Rimi")

            if not stores:
                error_message = "Please select at least one store."
                return render_template('result.html', results={}, user_data=user_data, store='none', error_message=error_message)

            store_preference = "both" if len(stores) == 2 else stores[0]

            cursor.execute("UPDATE lietotajs SET store_preference = %s WHERE id = %s", (store_preference, session['user_id']))
            connection.commit()
            user_data['store_preference'] = store_preference
        else:
            user_data['store_preference'] = user_data.get('store_preference', 'both')

        results = DIETcalc.calculate_diet(
            age=to_float(user_data['vecums']),
            height=to_float(user_data['augums']),
            weight=to_float(user_data['svars']),
            gender=1 if user_data['dzimums'] == 'vīrietis' else 0,
            selected_products=[product['id'] for product in user_data['selected_products']],
            user_max_limits=user_data['max_limits'],
            user_min_limits=user_data['min_limits'],
            store=user_data['store_preference']
        )

        if 'Error' in results:
            logging.error(f"Error from DIETcalc: {results['Error']}")
            if "No suitable products" in results['Error']:
                error_msg = "Too few products selected or dietary restrictions are too strict."
            elif "optimal solution" in results['Error']:
                error_msg = "No optimal solution found. Please adjust your dietary restrictions."
            else:
                error_msg = results['Error']
            return render_template('error.html', error_message=error_msg)

        return render_template('result.html', 
                               results=results, 
                               user_data=user_data, 
                               store=user_data['store_preference'], 
                               error_message=None, 
                               first_name=user_data['vards'], 
                               last_name=user_data['uzvards'])

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Database error occurred while calculating menu.")
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred.")

@user_bp.route('/update_selected_products', methods=['POST'])
def update_selected_products():

    """
    Funkcija lietotāja izvēlēto produktu atjaunināšanai.
    Apstrādā POST pieprasījumu un atjaunina sarakstu ar izvēlētajiem produktiem datubāzē.
    """

    if 'user_id' not in session:
        return {"error": "Unauthorized"}, 401

    data = request.get_json()
    product_id = str(data.get('product_id'))
    action = data.get('action')

    if not product_id or action not in ['add', 'remove']:
        return {"error": "Invalid request"}, 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT selected_products FROM lietotajs WHERE id = %s", (session['user_id'],))
        result = cursor.fetchone()
        selected_products = json.loads(result['selected_products'] or '[]')

        if action == 'add' and product_id not in selected_products:
            selected_products.append(product_id)
        elif action == 'remove' and product_id in selected_products:
            selected_products.remove(product_id)

        cursor.execute(
            "UPDATE lietotajs SET selected_products = %s WHERE id = %s",
            (json.dumps(selected_products), session['user_id'])
        )
        connection.commit()

        return {"success": True, "selected_products": selected_products}
    
    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return {"error": "Database error occurred while updating selected products"}, 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {"error": "An unexpected error occurred"}, 500
