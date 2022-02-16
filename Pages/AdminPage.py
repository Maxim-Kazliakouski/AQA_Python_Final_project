import time
# from Test.tests_AdminPage.test_for_Admin_page import TestDataAdminPage
from Test.tests_AdminPage.data_for_AdminPage import TestDataAdminPage
from Locators.main_page_locators import MainPageLocators
from Pages.BasePage import BasePage
from Locators.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def login_to_admin_page_under_admin(self):
        username_field = self.search_element(MainPageLocators.USERNAME_FIELD)
        username_field.send_keys(TestDataAdminPage.USER_NAME_FOR_ADMIN)
        password_field = self.search_element(MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(TestDataAdminPage.PASSWORD_FOR_ADMIN)
        login_button = self.search_element(MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def getting_user_name(self):
        user_name = self.search_element(AdminPageLocators.USER_NAME_ON_ADMIN_PAGE).text
        return user_name

    def go_to_group_tab(self):
        groups_tab = self.search_element(AdminPageLocators.GROUP_TAB)
        groups_tab.click()

    def go_to_users_tab(self):
        users_tab = self.search_element(AdminPageLocators.USERS_TAB)
        users_tab.click()

    def getting_group_list(self):
        group_list = self.search_element(AdminPageLocators.GROUP_LIST).text
        return group_list

    def getting_users_list(self):
        users_list = self.search_element(AdminPageLocators.USER_LIST).text
        return users_list

    def creating_user_without_any_statuses(self):
        adding_user_button = self.search_element(AdminPageLocators.ADDING_USER_BUTTON)
        adding_user_button.click()
        username_field = self.search_element(AdminPageLocators.USERNAME_FIELD)
        username_field.send_keys(TestDataAdminPage.USERNAME)
        password1_field = self.search_element(AdminPageLocators.PASSWORD_FIELD1)
        password1_field.send_keys(TestDataAdminPage.PASSWORD)
        password2_field = self.search_element(AdminPageLocators.PASSWORD_FIELD2)
        password2_field.send_keys(TestDataAdminPage.PASSWORD)
        save_button = self.search_element(AdminPageLocators.SAVE_BUTTON)
        save_button.click()

    def creating_user_with_staff_status(self):
        adding_user_button = self.search_element(AdminPageLocators.ADDING_USER_BUTTON)
        adding_user_button.click()
        username_field = self.search_element(AdminPageLocators.USERNAME_FIELD)
        username_field.send_keys(TestDataAdminPage.USERNAME)
        password1_field = self.search_element(AdminPageLocators.PASSWORD_FIELD1)
        password1_field.send_keys(TestDataAdminPage.PASSWORD)
        password2_field = self.search_element(AdminPageLocators.PASSWORD_FIELD2)
        password2_field.send_keys(TestDataAdminPage.PASSWORD)
        save_and_editing = self.search_element(AdminPageLocators.SAVE_AND_EDITING_BUTTON)
        save_and_editing.click()
        staff_status_checkbox = self.search_element(AdminPageLocators.STAFF_STATUS_CHECKBOX)
        staff_status_checkbox.click()
        save_button = self.search_element(AdminPageLocators.SAVE_BUTTON)
        save_button.click()

    def creating_user_with_all_statuses(self):
        adding_user_button = self.search_element(AdminPageLocators.ADDING_USER_BUTTON)
        adding_user_button.click()
        username_field = self.search_element(AdminPageLocators.USERNAME_FIELD)
        username_field.send_keys(TestDataAdminPage.USERNAME)
        password1_field = self.search_element(AdminPageLocators.PASSWORD_FIELD1)
        password1_field.send_keys(TestDataAdminPage.PASSWORD)
        password2_field = self.search_element(AdminPageLocators.PASSWORD_FIELD2)
        password2_field.send_keys(TestDataAdminPage.PASSWORD)
        save_and_editing = self.search_element(AdminPageLocators.SAVE_AND_EDITING_BUTTON)
        save_and_editing.click()
        staff_status_checkbox = self.search_element(AdminPageLocators.STAFF_STATUS_CHECKBOX)
        staff_status_checkbox.click()
        superuser_status_checkbox = self.search_element(AdminPageLocators.SUPERUSER_STATUS_CHECKBOX)
        superuser_status_checkbox.click()
        save_button = self.search_element(AdminPageLocators.SAVE_BUTTON)
        save_button.click()

    def user_settings(self):
        created_user = self.search_element(AdminPageLocators.CREATED_USER)
        created_user.click()

    def adding_user_to_group(self):
        group = self.search_element(AdminPageLocators.GROUP_NAME)
        # action = ActionChains(self.browser)
        # action.double_click(on_element=group)
        # action.perform()
        group.click()
        add_button = self.search_element(AdminPageLocators.ADD_BUTTON)
        add_button.click()
        save_button = self.search_element(AdminPageLocators.SAVE_BUTTON)
        save_button.click()

    def saving_variable(self, var):
        file_for_variable = open("Test/tests_AdminPage/var.txt",
                                 'w')
        file_for_variable.write(var)
        file_for_variable.close()

    def getting_user_id(self):
        user_id = []
        current_url_with_id = self.getting_current_url()
        new_http = current_url_with_id[38:]
        for i in new_http:
            if i == '/':
                break
            else:
                user_id.append(i)
        result = ''.join(user_id)
        return result

    def exiting_from_admin_panel(self):
        logout_button = self.search_element(AdminPageLocators.LOGOUT_BUTTON)
        logout_button.click()

    def login_again_button(self):
        login_again_button = self.search_element(AdminPageLocators.LOGIN_AGAIN_BUTTON)
        login_again_button.click()

    def login_to_admin_page_under_new_created_user(self):
        username_field = self.search_element(MainPageLocators.USERNAME_FIELD)
        username_field.send_keys(TestDataAdminPage.USERNAME)
        password_field = self.search_element(MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(TestDataAdminPage.PASSWORD)
        login_button = self.search_element(MainPageLocators.LOGIN_BUTTON)
        login_button.click()
