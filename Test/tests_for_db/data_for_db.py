from DataBase.data_for_connection import ConnectionToDB

varfile = open('Test/tests_AdminPage/var.txt')
user_id = str(varfile.read())


class TestDataDB:
    GROUP_NAME = 'Test group max'
    QUERY_FOR_ADDING_GROUP = """insert into auth_group (id, name) values (2, 'Test group max')"""
    QUERY_NAME_FOR_ADDING_GROUP = 'adding new group'
    SUCCESS_CONNECT = f"Connection to PostgreSQL DB '{ConnectionToDB.DB_NAME}' successful"
    SUCCESS_ADDING_NEW_GROUP = f"Query {QUERY_FOR_ADDING_GROUP} executed successfully"
    DELETING_NEW_GROUP = """delete from auth_group where id=2"""
    QUERY_FOR_GETTING_USERS_IN_GROUP = \
        """select id, user_id, group_id from auth_user_groups where user_id="""
    QUERY_FOR_DELETING_USER_FROM_GROUP = """delete from auth_user_groups where user_id="""
    SUCCESS_DELETING_USER_FROM_GROUP = f"Query {QUERY_FOR_DELETING_USER_FROM_GROUP} executed successfully"
    QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL = """delete from auth_user where id="""
    SUCCESS_DELETING_USER_FROM_ADMIN_PANEL = f"Query {QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL} executed successfully"
    QUERY_FOR_GETTING_INFO_BY_USER = """select id, is_superuser, username, first_name, last_name, email, is_staff, is_active from auth_user where id="""
    QUERY_FOR_GETTING_FIRST_CREATED_POST = """select min(id) from app_post"""
    QUERY_FOR_GETTING_POSTS_LIST = """select id from app_post"""
    DELETING_ALL_POSTS = """delete from app_post where id>3"""
    SUCCESS_DELETING_ALL_POSTS = f"Query {DELETING_ALL_POSTS} executed successfully"
    ADDING_POST_FOR_START_TEST = """insert into app_post (id, date, photo) values (1, '2022-02-09', 'Test photo') ON CONFLICT DO NOTHING"""
    ADDING_POST_FOR_START_TEST1 = """insert into app_post (id, date, photo) values (2, '2022-02-09', 'Test photo') ON CONFLICT DO NOTHING"""
    DELETING_ALL_USERS_FROM_GROUPS = """delete from auth_user_groups where id>86"""
    DELETING_ALL_USERS = """delete from auth_user where id>2"""
    DELETING_ALL_GROUPS = """delete from auth_user_groups *"""
