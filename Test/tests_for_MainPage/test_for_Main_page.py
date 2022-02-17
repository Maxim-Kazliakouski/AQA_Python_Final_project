# import sys
import Pages.MainPage as from_main_page

# sys.path.insert(0, '/Volumes/Work/Python_courses/Project/Final_project/Pages')
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
