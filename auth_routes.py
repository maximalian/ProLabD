from flask import Blueprint, render_template, request, redirect, url_for, session
from db import get_db_connection
from flask_bcrypt import Bcrypt
import psycopg2
import psycopg2.extras
import json
import logging

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth.route('/register', methods=['GET', 'POST'])
def register():

    """
    Lietotāju reģistrācijas funkcija.
    Apstrādā GET un POST pieprasījumus.
    - GET: Atgriež reģistrācijas veidlapu.
    - POST: Apstrādā reģistrācijas formu un saglabā jauno lietotāju datubāzē.
    """

    if request.method == 'POST':
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Lietotajs (epasts, parole, auth_provider)
                VALUES (%s, %s, 'email')
                RETURNING id
                """,
                (email, password)
            )
            result = cursor.fetchone()
            if result:
                user_id = result[0]
                session['user_id'] = user_id
                connection.commit()
                return redirect(url_for('auth.add_details'))
            else:
                raise Exception("Failed to retrieve user ID after registration.")
        
        except psycopg2.DatabaseError as db_error:
            logging.error(f"Database error during registration: {db_error}")
            return render_template('error.html', error_message="Failed to register due to database error.")
        except Exception as e:
            logging.error(f"Unexpected error during registration: {e}")
            return render_template('error.html', error_message=f"An unexpected error occurred: {e}")

    return render_template('register.html')


@auth.route('/add_details', methods=['GET', 'POST'])
def add_details():

    """
    Funkcija lietotāja datu pievienošanai un atjaunināšanai.
    Apstrādā GET un POST pieprasījumus.
    - GET: Atgriež veidlapu lietotāja datu ievadei.
    - POST: Apstrādā ievadītos datus un atjaunina datubāzi.
    """

    if 'user_id' not in session:
        return redirect(url_for('auth.register'))

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cursor.execute("SELECT * FROM lietotajs WHERE id = %s", (session['user_id'],))
        user = dict(cursor.fetchone())

        cursor.execute("SELECT * FROM produkts ORDER BY nosaukums")
        all_products = [dict(row) for row in cursor.fetchall()]
        cursor.execute("SELECT DISTINCT kategorija_key, nosaukums FROM kategorijas")
        all_categories = [dict(row) for row in cursor.fetchall()]

        if request.method == 'POST':
            name = request.form.get('name')
            surname = request.form.get('surname')
            gender = request.form.get('gender')
            weight = request.form.get('weight')
            height = request.form.get('height')
            age = request.form.get('age')

            min_limits = json.loads(request.form.get('min_limits', '{}'))
            max_limits = json.loads(request.form.get('max_limits', '{}'))
            excluded_products = json.loads(request.form.get('excluded_products', '[]'))

            filtered_min_limits = {k: v for k, v in min_limits.items() if v is not None and v != ""}
            filtered_max_limits = {k: v for k, v in max_limits.items() if v is not None and v != ""}

            cursor.execute(
                """
                UPDATE Lietotajs
                SET vards = %s, uzvards = %s, dzimums = %s, svars = %s, augums = %s, vecums = %s,
                    min_limits = %s, max_limits = %s, selected_products = %s
                WHERE id = %s
                """,
                (
                    name, surname, gender, weight, height, age,
                    json.dumps(filtered_min_limits), json.dumps(filtered_max_limits), json.dumps(excluded_products), session['user_id']
                )
            )
            connection.commit()
            return redirect(url_for('user_bp.calculate_menu'))

        return render_template('add_details.html', user=user, all_products=all_products, all_categories=all_categories)

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error while adding details: {db_error}")
        return render_template('error.html', error_message="Failed to add details due to database error.")
    except Exception as e:
        logging.error(f"Unexpected error while adding details: {e}")
        return render_template('error.html', error_message="An unexpected error occurred while adding details.")

@auth.route('/login', methods=['GET', 'POST'])
def login():

    """
    Lietotāja autentifikācijas funkcija.
    Apstrādā GET un POST pieprasījumus.
    - GET: Atgriež pieteikšanās formu.
    - POST: Pārbauda ievadīto e-pastu un paroli, lai autentificētu lietotāju.
    """

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        try:
            cursor.execute("SELECT * FROM Lietotajs WHERE epasts = %s", (email,))
            user = cursor.fetchone()

            if user and bcrypt.check_password_hash(user['parole'], password):
                session['user_id'] = user['id']
                session['user_name'] = user['vards']
                return redirect(url_for('user_bp.calculate_menu'))
            else:
                return render_template('index.html', error="Invalid credentials. Please try again.")
                
        except psycopg2.DatabaseError as db_error:
            logging.error(f"Database error during login: {db_error}")
            return render_template('error.html', error_message="Failed to log in due to database error.")
        except Exception as e:
            logging.error(f"Unexpected error during login: {e}")
            return render_template('error.html', error_message="An unexpected error occurred during login.")

    return render_template('index.html')

@auth.route('/logout')
def logout():

    """
    Funkcija, lai izrakstītu lietotāju no sistēmas.
    - Tiek notīrīta lietotāja sesija.
    - Pāradresē uz mājaslapu.
    """

    session.clear()
    return redirect(url_for('home'))
