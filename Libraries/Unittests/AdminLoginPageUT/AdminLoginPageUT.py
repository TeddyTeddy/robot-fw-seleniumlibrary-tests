import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator
from Credentials import DICT__CREDENTIALS
from AdminLoginPage import AdminLoginPage


class AdminLoginPageUT(unittest.TestCase):
    def setUp(self) -> None:
        LibraryLoaderStub.mock_library_loader_and_selenium_library()
        self._admin_login_page = AdminLoginPage()

    def test_login(self):
        self._admin_login_page.login(DICT__CREDENTIALS['valid_admin']['username'],
                                     DICT__CREDENTIALS['valid_admin']['password'])
        verify(LibraryLoader.get_instance().sl,
               times=1).input_text(locator=locator['admin_login_page']['username_field'], text='hakan')

    def tearDown(self) -> None:
        unstub()


if __name__ == '__main__':
    unittest.main()
