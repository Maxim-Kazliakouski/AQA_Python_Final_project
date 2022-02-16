# import sys
import time
import Pages.AdminPage as from_admin_page
# sys.path.insert(0, '/Volumes/Work/Python_courses/Project/Final_project/Pages')
import DataBase.PostgreSQL as DB
from Test.tests_for_db.data_for_db import TestDataDB
from Test.tests_AdminPage.data_for_AdminPage import TestDataAdminPage


class Test_for_admin_page:
    def test_user_on_login_page(self, browser, starting_clearing_closing_db, logs_admin_page):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        admin_login_page = page.getting_current_url()
        try:
            assert admin_login_page == TestDataAdminPage.ADMIN_PAGE_LOGIN_URL, "User isn't on the admin login page"
        except AssertionError as error:
            logs_admin_page.error("User isn't on the admin login page")
            raise error

    def test_user_is_logged_to_admin_page(self, browser, logs_admin_page):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        page.login_to_admin_page_under_admin()
        try:
            assert page.getting_user_name().lower() == TestDataAdminPage.USER_NAME_FOR_ADMIN, "User hasn't login to admin page"
        except AssertionError as error:
            logs_admin_page.error("User hasn't login to admin page")
            raise error

    def test_adding_new_group(self, browser, adding_new_group_via_db, logs_admin_page):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        page.login_to_admin_page_under_admin()
        page.go_to_group_tab()
        try:
            assert TestDataDB.GROUP_NAME in page.getting_group_list(), f"The '{TestDataDB.GROUP_NAME}' group hasn't been added!"
        except AssertionError as error:
            logs_admin_page.error(f"The '{TestDataDB.GROUP_NAME}' group hasn't been added!")
            raise error

    def test_creating_user(self, browser, deleting_user_from_admin_panel, logs_admin_page):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        page.login_to_admin_page_under_admin()
        page.creating_user_without_any_statuses()
        page.user_settings()
        user_id = page.getting_user_id()
        page.saving_variable(user_id)
        page.go_to_users_tab()
        page.getting_users_list()
        try:
            assert TestDataAdminPage.USERNAME in page.getting_users_list(), f"The user '{TestDataAdminPage.USERNAME}'" \
                                                                            f" hasn't been created"
        except AssertionError as error:
            logs_admin_page.error(f"The user '{TestDataAdminPage.USERNAME}' hasn't been created")
            raise error

    def test_adding_user_to_the_group(self, browser, deleting_user_from_group, logs_admin_page):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        page.login_to_admin_page_under_admin()
        page.creating_user_without_any_statuses()
        page.go_to_users_tab()
        page.user_settings()
        page.adding_user_to_group()
        page.user_settings()
        user_id = page.getting_user_id()
        page.saving_variable(user_id)
        connection_to_db = DB.connection
        request = DB.execute_read_query(connection_to_db, TestDataDB.QUERY_FOR_GETTING_USERS_IN_GROUP + user_id)
        response = DB.parsing_response(request)
        try:
            assert str(response[1]) == user_id, f"The user with ID = {user_id} hasn't been added to the group!"
        except AssertionError as error:
            logs_admin_page.error(f"The user with ID = {user_id} hasn't been added to the group!")
            raise error

    def test_creating_user_in_admin_panel(self, browser, logs_admin_page, deleting_user_from_admin_panel):
        link = TestDataAdminPage.ADMIN_PAGE_LOGIN_URL
        page = from_admin_page.AdminPage(browser, link)
        page.open_page(link)
        page.login_to_admin_page_under_admin()
        page.go_to_users_tab()
        page.creating_user_with_all_statuses()
        time.sleep(5)
        page.user_settings()
        user_id = page.getting_user_id()
        page.saving_variable(user_id)
        connection_to_db = DB.connection
        request = DB.execute_read_query(connection_to_db, TestDataDB.QUERY_FOR_GETTING_INFO_BY_USER + user_id)
        response = DB.parsing_response(request)
        try:
            assert str(response[0]) == user_id, f"The user {user_id} hasn't been created in admin panel"
        except AssertionError as error:
            logs_admin_page.error(f"The user {user_id} hasn't been created in admin panel")
            raise error
        page.exiting_from_admin_panel()
        page.login_again_button()
        page.login_to_admin_page_under_new_created_user()
        username = page.getting_user_name()
        try:
            assert username == TestDataAdminPage.USERNAME.upper(), f"The user '{TestDataAdminPage.USERNAME}' hasn't been logged"
        except AssertionError as error:
            logs_admin_page.error(f"The user '{TestDataAdminPage.USERNAME}' hasn't been logged")
            raise error
