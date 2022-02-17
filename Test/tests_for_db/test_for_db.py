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

    # def test_adding_new_group_via_db(self):
    #     request = DB.execute_query(DB.connection, TestDataDB.QUERY_FOR_ADDING_GROUP)
    #     assert request == TestDataDB.SUCCESS_ADDING_NEW_GROUP, "New group hasn't been added"


