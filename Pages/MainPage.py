import time
import Test.tests_AdminPage.data_for_AdminPage as data_admin
from Locators.admin_page_locators import AdminPageLocators
from Locators.main_page_locators import MainPageLocators
from Pages.BasePage import BasePage
import DataBase.PostgreSQL as DB
from Test.tests_for_MainPage.data_for_MainPage import TestData
from Test.tests_for_db.data_for_db import TestDataDB


class MainPage(BasePage):
    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def refreshing_page(self):
        self.browser.refresh()

    def go_to_admin_panel_as_admin(self):
        admin_button = self.search_element(MainPageLocators.GO_TO_ADMIN_BUTTON)
        admin_button.click()
        username_field = self.search_element(MainPageLocators.USERNAME_FIELD)
        username_field.send_keys(data_admin.TestDataAdminPage.USER_NAME_FOR_ADMIN)
        password_field = self.search_element(MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(data_admin.TestDataAdminPage.PASSWORD_FOR_ADMIN)
        login_button = self.search_element(MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def go_to_posts_tab(self):
        posts_tab = self.search_element(AdminPageLocators.POSTS_TAB)
        posts_tab.click()

    def getting_ID_first_created_post(self):
        first_created_post = self.search_element(AdminPageLocators.FIRST_CREATED_POST)
        first_created_post.click()

    def changing_date_for_post(self):
        date_field = self.search_element(AdminPageLocators.DATE_FIELD)
        date_field.clear()
        date_field.send_keys(TestData.DATE_FOR_POST)
        save_button = self.search_element(AdminPageLocators.SAVE_BUTTON)
        save_button.click()

    def deleting_first_created_post(self):
        delete_button = self.search_element(AdminPageLocators.DELETE_BUTTON)
        delete_button.click()
        submit_button = self.search_element(AdminPageLocators.YES_SURE_BUTTON)
        submit_button.click()

    def finding_post_by_date(self):
        try:
            self.search_element(MainPageLocators.POST_DATE)
            return True
        except:
            return False

    def getting_ID_posts_list(self):
        id_posts_list = []
        connection_to_db = DB.connection
        request = DB.execute_read_query(connection_to_db, TestDataDB.QUERY_FOR_GETTING_POSTS_LIST)
        for id in request:
            id_posts_list.append(id[0])
        print(id_posts_list)
        return id_posts_list

    # def getting_post_in_admin_panel(self):
    #     firs_post = self.search_element(AdminPageLocators.FIRST_CREATED_POST)
    #     firs_post.click()
