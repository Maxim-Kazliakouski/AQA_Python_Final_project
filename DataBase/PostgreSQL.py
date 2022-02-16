import psycopg2
from psycopg2 import OperationalError
from Tests.Tests_for_db.data_for_db import TestDataDB
from DataBase.data_for_connection import ConnectionToDB
from Pages.BasePage import BasePage


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


# # data base creation
# def create_database(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# create_database_query = "CREATE DATABASE users"
#
#
# # create_database(connection, create_database_query)
#
#


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


# # -----------------------------------------------------------------------------------
#
# # creating table in database
# create_users_table = """
# CREATE TABLE IF NOT EXISTS test_users (
#   id SERIAL PRIMARY KEY,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# )
# """
# # execute_query(connection, create_users_table)
#
# # -----------------------------------------------------------------------------------
#
# # inserting data into the table
# users = [
#     ("James", 25, "male", "USA"),
#     ("Leila", 32, "female", "France"),
#     ("Brigitte", 35, "female", "England"),
#     ("Mike", 40, "male", "Denmark"),
#     ("Elizabeth", 21, "female", "Canada"),
# ]
#
# user_records = ", ".join(["%s"] * len(users))
#
# insert_query = (
#     f"INSERT INTO test_users (name, age, gender, nationality) VALUES {user_records}"
# )
#
# # connection.autocommit = True
# # cursor = connection.cursor()
# # cursor.execute(insert_query, users)
#
# # -----------------------------------------------------------------------------------
#
#
# # getting data from table
# select_users = "SELECT * FROM test_users"
# users = execute_read_query(connection, select_users)
#
# for user in users:
#     print(user)
# # -----------------------------------------------------------------------------------
#
# query for outputting all tables in database

tables_info = """
SELECT n.nspname, c.relname
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r' AND n.nspname NOT IN('pg_catalog', 'information_schema');
"""
# info = execute_read_query(connection, tables_info)
# for each_row in info:
#     print(each_row)

# adding new group:
# query = TestDataDB.QUERY_FOR_ADDING_GROUP
# execute_query(connection, TestDataDB.QUERY_FOR_ADDING_GROUP)
# execute_query(connection, TestDataDB.DELETING_NEW_GROUP)
