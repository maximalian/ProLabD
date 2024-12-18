import psycopg2
import logging
from dotenv import load_dotenv
from contextlib import contextmanager
import os

load_dotenv()

DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

@contextmanager
def database_connection():
    connection = get_db_connection()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        yield cursor
        connection.commit()
    except psycopg2.DatabaseError as db_error:
        logging.error(f"Database error: {db_error}")
        raise 
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise
    finally:
        cursor.close()
        connection.close()
