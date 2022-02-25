import Pages.MainPage as from_main_page
from Locators.main_page_locators import MainPageLocators
from Test.tests_for_MainPage.data_for_MainPage import TestData


class Test_for_main_page:
    class Test_positive:
        def test_user_on_main_page(self, browser, adding_posts, starting_closing_db, logs_main_page):
            """This case checks that user is on main page"""
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
            """This case checks that created image has been deleted from main page """
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            # refreshing page for creating additional posts
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
            """This case checks, that contact info is present on main page"""
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
            """This case checks, that about info is present on main page"""
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
            """This case checks, that after clicking on ALBUM button user redirects to the album page"""
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

        def test_default_name_password(self, browser, logs_main_page):
            """This case checks, that on the page there is default username and password"""
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            info = page.getting_default_username_password()
            try:
                assert info == f"(ID:{TestData.USER_NAME_FOR_ADMIN}, PW:{TestData.PASSWORD_FOR_ADMIN})",\
                    "There is no default admin name and password on main page"
            except AssertionError as err:
                logs_main_page("There is no default admin name and password on main page")
                raise err

        def test_adding_image_after_refreshing_page(self, browser, logs_main_page):
            """This case checks, that after refreshing page the image is adding"""
            link = TestData.MAINPAGE_URL
            page = from_main_page.MainPage(browser, link)
            page.open_page(TestData.MAINPAGE_URL)
            amount_of_images = page.getting_amount_of_images()
            page.refreshing_page()
            amount_of_images_after_refreshing = page.getting_amount_of_images()
            try:
                assert int(amount_of_images_after_refreshing) == int(amount_of_images) + 1,\
                    "The image doesn't add after refreshing"
            except AssertionError as err:
                logs_main_page("The image doesn't add after refreshing")
                raise err
