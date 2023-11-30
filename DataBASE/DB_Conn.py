import psycopg2.extensions
from psycopg2.extras import RealDictCursor
from psycopg2 import pool

db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    user='postgres',
    password='Ankit123@post',
    database='Goat',
    host='localhost',
    port='8003',
    cursor_factory=RealDictCursor
)


def execute_on_database(query):
    connection = db_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(f"Error in Database thing: {e}")
    finally:
        cursor.close()
        db_pool.putconn(connection)


def insert_on_database(querry , values):
    connection = db_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute(querry , values)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Error in Database thing: {e}")
    finally:
        connection.commit()
        cursor.close()
        db_pool.putconn(connection)