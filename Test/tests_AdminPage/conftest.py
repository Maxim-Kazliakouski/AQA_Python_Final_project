import time
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
# import sys
# sys.path.insert(0, '/Volumes/Work/Python_courses/Project/Final_project')
import DataBase.PostgreSQL as DB
from DataBase.data_for_connection import ConnectionToDB
from Test.tests_for_db.data_for_db import TestDataDB


@pytest.fixture(scope='class')
def starting_clearing_closing_db():
    print(f'\nConnecting to BD {ConnectionToDB.DB_NAME}...')
    connection = DB.create_connection(ConnectionToDB.DB_NAME,
                                      ConnectionToDB.DB_USER,
                                      ConnectionToDB.DB_PASSWORD,
                                      ConnectionToDB.DB_HOST)
    print('Deleting users from groups and deleting users from db...')
    try:
        DB.execute_query(connection, TestDataDB.DELETING_ALL_USERS_FROM_GROUPS)
    except:
        raise print("Users haven't been deleted from groups")
    try:
        DB.execute_query(connection, TestDataDB.DELETING_ALL_USERS)
    except:
        raise print("Users haven't been deleted")
    yield
    print('Deleting new created group via database...')
    try:
        DB.execute_query(connection, TestDataDB.DELETING_NEW_GROUP)
    except:
        raise print("New group hasn't been deleted")
    try: DB.execute_query(connection, TestDataDB.DELETING_ALL_GROUPS)
    except:
        raise print("All groups hasn't been deleted")
    connection.close()


@pytest.fixture(scope='function')
def adding_new_group_via_db():
    connection = DB.create_connection(ConnectionToDB.DB_NAME,
                                      ConnectionToDB.DB_USER,
                                      ConnectionToDB.DB_PASSWORD,
                                      ConnectionToDB.DB_HOST)
    print('\nAdding new group via database')
    request = DB.execute_query(connection, TestDataDB.QUERY_FOR_ADDING_GROUP)
    assert request == TestDataDB.SUCCESS_ADDING_NEW_GROUP, "New group hasn't been added"


@pytest.fixture(scope='function')
def deleting_user_from_group():
    print('Connected to the db for deleting user...')
    connection = DB.create_connection(ConnectionToDB.DB_NAME,
                                      ConnectionToDB.DB_USER,
                                      ConnectionToDB.DB_PASSWORD,
                                      ConnectionToDB.DB_HOST)

    yield
    print('\nPreparing db for deleting user from group...')
    print('Deleting user from group...')
    varfile = open('Test/tests_AdminPage/var.txt')
    user_id = str(varfile.read())
    success = f"Query {TestDataDB.QUERY_FOR_DELETING_USER_FROM_GROUP + user_id} executed successfully"
    request = DB.execute_query(connection, TestDataDB.QUERY_FOR_DELETING_USER_FROM_GROUP + user_id)
    assert request == success, "User hasn't been deleted!"
    success2 = f"Query {TestDataDB.QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL + user_id} executed successfully"
    request = DB.execute_query(connection, TestDataDB.QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL + user_id)
    assert request == success2, "User hasn't been deleted from admin panel!"
    varfile.close()
    # DB.connection.close()


@pytest.fixture(scope='function')
def deleting_user_from_admin_panel():
    print('Connected to the db for deleting user...')
    connection = DB.create_connection(ConnectionToDB.DB_NAME,
                                      ConnectionToDB.DB_USER,
                                      ConnectionToDB.DB_PASSWORD,
                                      ConnectionToDB.DB_HOST)

    yield
    print('\nPreparing db for deleting user from admin panel...')
    print('\nDeleting user from admin panel...')

    varfile = open('Test/tests_AdminPage/var.txt')
    ID_USER = str(varfile.read())
    success = f"Query {TestDataDB.QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL + ID_USER} executed successfully"
    request = DB.execute_query(connection, TestDataDB.QUERY_FOR_DELETING_USER_FROM_ADMIN_PANEL + ID_USER)
    assert request == success, "User hasn't been deleted from admin panel!"
    # DB.connection.close()


@pytest.fixture(scope='function')
def logs_admin_page():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('./logfile.log', mode='a', delay=False)
    # Formatter class to set the format of log file
    formatter = logging.Formatter(
        "[%(asctime)s] -- [%(levelname)s][%(lineno)d]--[%(name)s->tests_AdminPage]: \n%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    return logger


def pytest_addoption(parser):
    parser.addoption('--browser.name', action='store', default='chrome',
                     help="Choose browser: chrome or safari")
    parser.addoption('--headmode', action='store', default='true',
                     help='Choose turn on or turn off headless mode')
    # parser.addoption('--language', action='store', default=None,
    #                  help='Choose language: ru, en...(etc)')


@pytest.fixture(scope='session')
def clearing_results_folder():
    print('\nClearing results folder...')
    time.sleep(2)
    os.system("rm -rf /Volumes/MacOS/Users/max_kazliakouski/.jenkins/workspace/Final_project/allure-results/*")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser.name')
    headless = request.config.getoption('headmode')
    # opt = Options()
    # opt.add_argument("--disable-infobars")
    # opt.add_argument("start-maximized")
    # opt.add_argument("--disable-extensions")
    # opt.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    print(f'\nStarting browser {browser_name}...')
    global browser
    # user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # here we set in commandline choosing for headless mode
        if headless == 'true':
            options = webdriver.ChromeOptions()
            # adding browser options!!! important
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            # options.add_argument("--disable-notifications")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = True
            s = Service('Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            # params for docker
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            # s = Service('/usr/local/bin/chromedriver')
            # browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
        else:
            # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")
            options.headless = False
            s = Service('/Volumes/Work/Python_courses/Project/POM/Tools/chromedriver')
            browser = webdriver.Chrome(service=s, options=options)
            browser.maximize_window()
            browser.implicitly_wait(5)
    elif browser_name == 'safari':
        if headless == 'true':
            # options = webdriver.Safari()
            # options.headless = True
            browser = webdriver.Safari()
        else:
            # fp = webdriver.FirefoxProfile(options=options)
            # fp.set_preference("intl.accept_languages", user_language)
            # browser = webdriver.Firefox(executable_path='/Users/maxkazliakouski/Downloads/geckodriver')
            browser = webdriver.Safari()
            browser.maximize_window()
            print(f'Start {browser_name} browser for test...')
    else:
        print(f'Browser {browser_name} still not implemented')

    yield browser
    print(f'\nQuit browser {browser_name}...')
    # browser quit don't fit for safari, get the error about refuse connection
    browser.quit()
