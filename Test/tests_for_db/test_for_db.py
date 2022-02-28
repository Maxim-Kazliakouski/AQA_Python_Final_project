from Test.tests_for_db.data_for_db import TestDataDB
import DataBase.PostgreSQL as DB
from DataBase.data_for_connection import ConnectionToDB


class Test_for_databases:
    def test_connection_to_db(self):
        connection = DB.create_connection_for_test(ConnectionToDB.DB_NAME,
                                                   ConnectionToDB.DB_USER,
                                                   ConnectionToDB.DB_PASSWORD,
                                                   ConnectionToDB.DB_HOST)
        assert connection == TestDataDB.SUCCESS_CONNECT, f"User doesn't connect to database {ConnectionToDB.DB_NAME}"


