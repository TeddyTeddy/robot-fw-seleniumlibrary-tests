import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator
from Credentials import DICT__CREDENTIALS
from AdminLoginPage import AdminLoginPage
from ExpectedLinks import admin_login_page_url
from ExpectedTexts import expected


class AdminLoginPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        pass

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    def test_go_to_admin_login_page(self):
        # configure the mock selenium library for go_to_admin_login_page()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='go_to_admin_login_page')
        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_login_page = AdminLoginPage()

        # method under test gets called
        admin_login_page.go_to_admin_login_page()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).go_to(url=admin_login_page_url)

        verify(LibraryLoader.get_instance().sl, times=1).wait_until_element_is_enabled(
            locator=locator['admin_login_page']['login_button'])

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_login_page']['title'],
            expected=expected['admin_login_page']['title_text'])

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_login_page']['username_title'],
            expected=expected['admin_login_page']['username_text'])

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['admin_login_page']['password_title'],
            expected=expected['admin_login_page']['password_text'])

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['admin_login_page']['login_button'],
            attribute='value',
            expected=expected['admin_login_page']['login_button_text'])

    def test_login(self):
        # configure the mock selenium library for login()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='login')
        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_login_page = AdminLoginPage()

        # method under test gets called
        admin_login_page.login(DICT__CREDENTIALS['valid_admin']['username'],
                               DICT__CREDENTIALS['valid_admin']['password'])

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).input_text(
            locator=locator['admin_login_page']['username_field'],
            text=DICT__CREDENTIALS['valid_admin']['username'])

        verify(LibraryLoader.get_instance().sl, times=1).input_password(
            locator=locator['admin_login_page']['password_field'],
            password=DICT__CREDENTIALS['valid_admin']['password'])

        verify(LibraryLoader.get_instance().sl, times=1).click_element(
            locator=locator['admin_login_page']['login_button'])


if __name__ == '__main__':
    unittest.main()
