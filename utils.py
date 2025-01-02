import logging
from decimal import Decimal

def to_float(value):
    """
    Funkcija, lai droši konvertētu vērtību uz float formātu.
    - Apstrādā Decimal un None datus.
    """
    if isinstance(value, Decimal):
        return float(value)
    return float(value) if value is not None else 0.0

def get_next_id(cursor, table, id_column="id"):
    """
    Funkcija, lai iegūtu nākamo ID no norādītās tabulas.
    """
    cursor.execute(f"SELECT COALESCE(MAX({id_column}), 0) + 1 FROM {table}")
    return cursor.fetchone()[0]

def check_duplicate(cursor, table, column, value):
    """
    Funkcija, lai pārbaudītu, vai datubāzē pastāv dublikāts.
    """
    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = %s", (value,))
    return cursor.fetchone()[0] > 0

def validate_links(links, valid_prefixes):
    """
    Funkcija, lai validētu saites, pārbaudot prefiksus.
    """
    errors = []
    for link_key, link_value in links.items():
        if link_value and not any(link_value.startswith(prefix) for prefix in valid_prefixes):
            errors.append(f"{link_key} has an invalid link.")
    return errors

def safe_number(value):
    """
    Funkcija, lai droši konvertētu vērtību uz skaitlisko formātu.
    """
    try:
        return float(value) if value else None
    except ValueError:
        return None

def handle_database_error(db_error):
    """
    Funkcija, lai apstrādātu datubāzes kļūdas.
    """
    logging.error(f"Database error: {db_error}")
    return {"error": "Database operation failed due to a database error."}, 500