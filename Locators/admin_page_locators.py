from selenium.webdriver.common.by import By

from Test.tests_AdminPage.data_for_AdminPage import TestDataAdminPage
import DataBase.PostgreSQL as DB
from Test.tests_for_db.data_for_db import TestDataDB

connection_to_db = DB.connection
request = DB.execute_read_query(connection_to_db, TestDataDB.QUERY_FOR_GETTING_FIRST_CREATED_POST)
response = DB.parsing_response(request)
id = response[0]


class AdminPageLocators:
    GROUP_TAB = By.XPATH, "//a[contains(text(),'Groups')]"
    USERS_TAB = By.XPATH, "//tbody/tr[2]/th[1]/a[1]"
    POSTS_TAB = By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/th/a'
    GROUP_LIST = By.XPATH, '//*[@id="result_list"]/tbody'
    USER_LIST = By.XPATH, '//*[@id="result_list"]/tbody'
    USER_NAME_ON_ADMIN_PAGE = By.XPATH, '//*[@id="user-tools"]/strong'
    ADDING_USER_BUTTON = By.XPATH, "//tbody/tr[2]/td[1]/a[1]"
    USERNAME_FIELD = By.NAME, 'username'
    PASSWORD_FIELD1 = By.NAME, 'password1'
    PASSWORD_FIELD2 = By.NAME, 'password2'
    SAVE_BUTTON = By.CSS_SELECTOR, 'input[value="Save"]'
    CREATED_USER = By.XPATH, f"//a[contains(text(),'{TestDataAdminPage.USERNAME}')]"
    GROUP_NAME = By.XPATH, "//option[contains(text(),'New group')]"
    ADD_BUTTON = By.ID, "id_groups_add_link"
    LOGOUT_BUTTON = By.XPATH, '//*[@id="user-tools"]/a[3]'
    LOGIN_AGAIN_BUTTON = By.XPATH, '//*[@id="content"]/p[2]/a'
    STAFF_STATUS_CHECKBOX = By.XPATH, '//*[@id="user_form"]/div/fieldset[3]/div[2]/div/label'
    SUPERUSER_STATUS_CHECKBOX = By.XPATH, '//*[@id="user_form"]/div/fieldset[3]/div[3]/div/label'
    SAVE_AND_EDITING_BUTTON = By.XPATH, '//*[@id="user_form"]/div/div/input[3]'
    POSTS = By.XPATH, '//*[@id="result_list"]/tbody'
    FIRST_CREATED_POST = By.XPATH, f"//a[contains(text(),'Post object ({id})')]"
    DATE_FIELD = By.XPATH, '//*[@id="id_date_0"]'
    DELETE_BUTTON = By.CLASS_NAME, 'deletelink'
    YES_SURE_BUTTON = By.CSS_SELECTOR, 'input[value="Yes, I’m sure"]'
    ERROR_MESSAGE_DURING_REG_WITHOUT_USERNAME = By.XPATH, "//p[contains(text(),'Please correct the error below.')]"
    ERROR_MESSAGE_DURING_REG_WITHOUT_PASSWORDS_AT_ALL = By.XPATH, "//p[contains(text(),'Please correct the errors below.')]"
    ERROR_MESSAGE_DURING_REG_WITHOUT_CONFIRMED_PASSWORD = By.XPATH, "//p[contains(text(),'Please correct the error below.')]"
    ERROR_MESSAGE_FORBIDDEN_SYMBOLS_DURING_REG_USERNAME = By.XPATH, '//*[@id="user_form"]/div/fieldset/div[1]/ul/li'
