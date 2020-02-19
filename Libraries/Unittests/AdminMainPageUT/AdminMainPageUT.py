import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator
from Credentials import DICT__CREDENTIALS
from AdminMainPage import AdminMainPage     # class under test (CUT)
from ExpectedLinks import expected_admin_main_page_url
from ExpectedTexts import expected


class AdminMainPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        pass

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    def test_go_to_admin_main_page(self):
        # configure the mock selenium library for go_to_admin_login_page()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='go_to_admin_main_page')
        # CUT gets magically the mock instances (i.e. _loader & sl)
        admin_login_page = AdminMainPage()

        # method under test gets called
        admin_login_page.go_to_admin_main_page()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).go_to(expected_admin_main_page_url)


if __name__ == '__main__':
    unittest.main()
