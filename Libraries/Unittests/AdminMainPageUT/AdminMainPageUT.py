import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from SeleniumLibraryStub import configure_mock_calls_in_go_to_admin_main_page
from SeleniumLibraryStub import configure_mock_calls_in_verify_admin_main_page
from SeleniumLibraryStub import configure_mock_calls_in_click_on_add_group_button
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from Credentials import DICT__CREDENTIALS
from AdminMainPage import AdminMainPage     # class under test (CUT)
from ExpectedLinks import expected_admin_main_page_url, links
from ExpectedTexts import expected


class AdminMainPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    def test_go_to_admin_main_page(self):
        # configure the mock selenium library for go_to_admin_main_page()'s calls
        configure_mock_calls_in_go_to_admin_main_page(sl=LibraryLoader.get_instance().sl)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.go_to_admin_main_page()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).go_to(expected_admin_main_page_url)

    def test_verify_admin_main_page(self):
        # configure the mock selenium library for verify_admin_main_page()'s calls
        configure_mock_calls_in_verify_admin_main_page(sl=LibraryLoader.get_instance().sl)
        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.verify_admin_main_page(username=DICT__CREDENTIALS['valid_admin']['username'])

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).wait_until_element_is_enabled(
            locator=locator['admin_main_page']['logout'])

        verify(LibraryLoader.get_instance().sl, times=1).get_location()

        # verify texts
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['main_title'],
            expected=expected['admin_main_page']['main_title_text']
        )

        # user navigation bar on the upper right of the page
        dynamic_user_tab_text = expected['admin_main_page']['dynamic_user_tab_text'] % DICT__CREDENTIALS['valid_admin']['username'].upper()
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['welcome_user_x'],
            expected=dynamic_user_tab_text
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['view_site'],
            expected=expected['admin_main_page']['view_site_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['change_password'],
            expected=expected['admin_main_page']['change_password_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['logout'],
            expected=expected['admin_main_page']['logout_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['site_administration'],
            expected=expected['admin_main_page']['site_administration_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['authentication_and_authorization'],
            expected=expected['admin_main_page']['authentication_and_authorization_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['groups'],
            expected=expected['admin_main_page']['groups_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['users'],
            expected=expected['admin_main_page']['users_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['postings'],
            expected=expected['admin_main_page']['postings_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['blog_posts'],
            expected=expected['admin_main_page']['blog_posts_text']
        )

        # the number of 'Add' buttons must be number_of_add_buttons
        verify(LibraryLoader.get_instance().sl, times=1).page_should_contain_element(
            locator=locator['admin_main_page']['add_button'],
            limit=number_of_add_buttons
        )

        # the number of 'Change' buttons must be number_of_change_buttons
        verify(LibraryLoader.get_instance().sl, times=1).page_should_contain_element(
            locator=locator['admin_main_page']['change_button'],
            limit=number_of_change_buttons
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['recent_actions'],
            expected=expected['admin_main_page']['recent_actions_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_main_page']['my_actions'],
            expected=expected['admin_main_page']['my_actions_text']
        )

        # verify links
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['main_title'],
            attribute='href',
            expected=links['admin_main_page']['main_title_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['view_site'],
            attribute='href',
            expected=links['admin_main_page']['view_site_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['change_password'],
            attribute='href',
            expected=links['admin_main_page']['change_password_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['logout'],
            attribute='href',
            expected=links['admin_main_page']['logout_link']
        )

        # authentication and authorization section
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['authentication_and_authorization'],
            attribute='href',
            expected=links['admin_main_page']['authentication_and_authorization_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['groups'],
            attribute='href',
            expected=links['admin_main_page']['groups_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['users'],
            attribute='href',
            expected=links['admin_main_page']['users_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['add_group'],
            attribute='href',
            expected=links['admin_main_page']['add_group_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['change_group'],
            attribute='href',
            expected=links['admin_main_page']['change_group_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['add_user'],
            attribute='href',
            expected=links['admin_main_page']['add_user_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['change_user'],
            attribute='href',
            expected=links['admin_main_page']['change_user_link']
        )

        # postings section
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['postings'],
            attribute='href',
            expected=links['admin_main_page']['postings_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['blog_posts'],
            attribute='href',
            expected=links['admin_main_page']['blog_posts_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['add_blog_post'],
            attribute='href',
            expected=links['admin_main_page']['add_blog_post_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_main_page']['change_blog_post'],
            attribute='href',
            expected=links['admin_main_page']['change_blog_post_link']
        )

    def test_click_on_add_group_button(self):
        # configure the mock selenium library for click_on_add_group_button()'s calls
        configure_mock_calls_in_click_on_add_group_button(sl=LibraryLoader.get_instance().sl)
        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_main_page = AdminMainPage()

        # method under test gets called
        admin_main_page.click_on_add_group_button()

        verify(LibraryLoader.get_instance().sl, times=1).click_link(
            locator=locator['admin_main_page']['add_group']
        )


if __name__ == '__main__':
    unittest.main()
