from flask import Blueprint, request, render_template, redirect
from db import get_db_connection
import psycopg2
import logging


product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/manage_products', methods=['GET'])
def manage_products():

    """
    Funkcija, lai pārvaldītu produktus.
    - Apstrādā GET pieprasījumu.
    - Iegūst visu produktu un kategoriju sarakstu no datubāzes.
    - Atgriež HTML veidni ar produktu datiem.
    """

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cursor.execute("""
            SELECT 
                p.id, p.nosaukums, p.kalorijas, p.olbaltumvielas, p.tauki, 
                p.oglhidrati, p.cena_maxima, p.cena_rimi, p.saite_maxima,
                p.saite_rimi, p.meris_vieniba, c.nosaukums AS category_name,
                p.kategorija_key, p.vegan, p.failed_urls
            FROM produkts p
            LEFT JOIN kategorijas c ON p.kategorija_key = c.kategorija_key
            ORDER BY p.nosaukums
        """)
        products = [dict(row) for row in cursor.fetchall()]

        cursor.execute("SELECT kategorija_key, nosaukums FROM kategorijas ORDER BY nosaukums")
        categories = [dict(row) for row in cursor.fetchall()]

        return render_template('manage_products.html', all_products=products, categories=categories)

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Failed to load products due to a database error.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred while loading the products.")

@product_bp.route('/update_product', methods=['POST'])
def update_product():

    """
    Funkcija, lai atjauninātu produkta informāciju.
    Apstrādā POST pieprasījumu un atjaunina produkta datus datubāzē.
    """

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        product_id = request.form.get('id')
        nosaukums = request.form.get('nosaukums')
        kalorijas = request.form.get('kalorijas') or None
        olbaltumvielas = request.form.get('olbaltumvielas') or None
        tauki = request.form.get('tauki') or None
        oglhidrati = request.form.get('oglhidrati') or None
        cena_maxima = request.form.get('cena_maxima')
        cena_maxima = None if not cena_maxima or cena_maxima == 'null' else float(cena_maxima)

        cena_rimi = request.form.get('cena_rimi')
        cena_rimi = None if not cena_rimi or cena_rimi == 'null' else float(cena_rimi)

        saite_maxima = request.form.get('saite_maxima') or None
        saite_rimi = request.form.get('saite_rimi') or None
        meris_vieniba = request.form.get('meris_vieniba') or None
        kategorija_key = request.form.get('kategorija_key') or None
        vegan = request.form.get('vegan') or None

        cursor.execute("""
            UPDATE produkts SET 
                nosaukums=%s, kalorijas=%s, olbaltumvielas=%s, tauki=%s, oglhidrati=%s,
                cena_maxima=%s, cena_rimi=%s, saite_maxima=%s, saite_rimi=%s,
                meris_vieniba=%s, kategorija_key=%s, vegan=%s
            WHERE id=%s
        """, (
            nosaukums, kalorijas, olbaltumvielas, tauki, oglhidrati,
            cena_maxima, cena_rimi, saite_maxima, saite_rimi,
            meris_vieniba, kategorija_key, vegan, product_id
        ))
        connection.commit()

        return "Product successfully updated!", 200

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Failed to update product due to a database error.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred while updating the product.")

@product_bp.route('/add_product', methods=['POST'])
def add_product():

    """
    Funkcija, lai pievienotu jaunu produktu datubāzei.
    Apstrādā POST pieprasījumu un ievieto jaunā produkta datus.
    """

    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        nosaukums = request.form.get('nosaukums')
        kalorijas = request.form.get('kalorijas')
        olbaltumvielas = request.form.get('olbaltumvielas')
        tauki = request.form.get('tauki')
        oglhidrati = request.form.get('oglhidrati')
        cena_maxima = request.form.get('cena_maxima') or None
        cena_rimi = request.form.get('cena_rimi') or None
        saite_maxima = request.form.get('saite_maxima') or None
        saite_rimi = request.form.get('saite_rimi') or None
        meris_vieniba = request.form.get('meris_vieniba')
        kategorija_key = request.form.get('kategorija_key') or None
        vegan = request.form.get('vegan') or None

        if not nosaukums or not kalorijas or not olbaltumvielas or not tauki or not oglhidrati or not meris_vieniba:
            return redirect('/product_bp/manage_products')

        cursor.execute(
            """
            INSERT INTO produkts (
                nosaukums, kalorijas, olbaltumvielas, tauki, oglhidrati,
                cena_maxima, cena_rimi, saite_maxima, saite_rimi,
                meris_vieniba, kategorija_key, vegan
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                nosaukums, kalorijas, olbaltumvielas, tauki, oglhidrati,
                cena_maxima, cena_rimi, saite_maxima, saite_rimi,
                meris_vieniba, kategorija_key, vegan
            )
        )
        connection.commit()
        return redirect('/product_bp/manage_products')

    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Failed to add product due to a database error.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred while adding the product.")

@product_bp.route('/delete_product', methods=['POST'])
def delete_product():

    """
    Funkcija, lai dzēstu produktu no datubāzes.
    Apstrādā POST pieprasījumu, izmantojot produkta ID.
    """

    product_id = request.form.get('product_id')
    if not product_id:
        return "Missing product ID", 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM produkts WHERE id = %s", (product_id,))
        connection.commit()
        return "Product deleted", 200
    
    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        return render_template('error.html', error_message="Failed to delete product due to a database error.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return render_template('error.html', error_message="An unexpected error occurred while deleting the product.")
