# import sys
import Pages.MainPage as from_main_page

# sys.path.insert(0, '/Volumes/Work/Python_courses/Project/Final_project/Pages')
from Locators.main_page_locators import MainPageLocators
from Test.tests_for_MainPage.data_for_MainPage import TestData


class Test_for_main_page:
    class Test_positive:
        def test_user_on_main_page(self, browser, adding_posts, starting_closing_db, logs_main_page):
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            main_page_url = page.getting_current_url()
            try:
                assert main_page_url == TestData.MAINPAGE_URL, "User isn't on Main Page"
            except AssertionError as err:
                logs_main_page.error("User isn't on Main Page")
                raise err

        def test_deleting_first_created_image_on_main_page(self, browser, deleting_all_posts, logs_main_page):
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            page.refreshing_page()
            page.go_to_admin_panel_as_admin()
            page.go_to_posts_tab()
            page.getting_ID_first_created_post()
            page.changing_date_for_post()
            page.getting_ID_first_created_post()
            page.deleting_first_created_post()
            page.open_page(TestData.MAINPAGE_URL)
            try:
                assert page.finding_post_by_date() == False, f"There is first created post by date {TestData.DATE_FOR_POST}"
            except AssertionError as err:
                logs_main_page.error(f"There is first created post by date {TestData.DATE_FOR_POST}")
                raise err

        def test_checking_contact_on_main_page(self, browser, logs_main_page):
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            contact_list = page.getting_contacts_list_from_main_page()
            try:
                assert contact_list == TestData.CONTACT_LIST, "There is no all contacts: Twitter, FaceBook, Email"
            except AssertionError as err:
                logs_main_page.error(f"There is no all contacts: {TestData.CONTACT_LIST}")
                raise err

        def test_checking_about_info(self, browser, logs_main_page):
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            about_info = page.getting_about_info()
            try:
                assert about_info == True, "About info is present"
            except AssertionError as err:
                logs_main_page("About info is present")
                raise err

        def test_redirection_to_the_album(self, browser, logs_main_page):
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            page.click_on_element(MainPageLocators.ALBUM_BUTTON)
            album_page_url = page.getting_current_url()
            try:
                assert album_page_url == TestData.ALBUM_PAGE_URL, "User isn't on album page"
            except AssertionError as err:
                logs_main_page("User isn't on album page")
                raise err


