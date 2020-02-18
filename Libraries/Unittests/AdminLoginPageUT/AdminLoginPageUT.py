import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator
from Credentials import DICT__CREDENTIALS
from AdminLoginPage import AdminLoginPage


class AdminLoginPageUT(unittest.TestCase):
    def setUp(self) -> None:
        LibraryLoaderStub.configure_mock_library_loader()
        self._admin_login_page = AdminLoginPage()

    def test_login(self):
        # function under test gets called
        self._admin_login_page.login(DICT__CREDENTIALS['valid_admin']['username'],
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

    def tearDown(self) -> None:
        unstub()


if __name__ == '__main__':
    unittest.main()
