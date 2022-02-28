import psycopg2
from psycopg2 import OperationalError
from DataBase.data_for_connection import ConnectionToDB


# connection to the database for testing
def create_connection_for_test(db_name, db_user, db_password, db_host):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host
            # port=db_port,
        )
        print(f"Connection to PostgreSQL DB '{db_name}' successful")
        result = f"Connection to PostgreSQL DB '{db_name}' successful"
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        result = f"The error '{e}' occurred"
    return result


def create_connection(db_name, db_user, db_password, db_host):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host
            # port=db_port,
        )
        print(f"Connection to PostgreSQL DB '{db_name}' successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(ConnectionToDB.DB_NAME,
                               ConnectionToDB.DB_USER,
                               ConnectionToDB.DB_PASSWORD,
                               ConnectionToDB.DB_HOST)


# reading data from table
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# executing query
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = f"Query {query} executed successfully"
    except OperationalError as e:
        result = f"The error '{e}' occurred"
    return result


def parsing_response(request):
    for element in request:
        return element


tables_info = """
SELECT n.nspname, c.relname
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r' AND n.nspname NOT IN('pg_catalog', 'information_schema');
"""
