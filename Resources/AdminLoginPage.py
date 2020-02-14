from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from Locators import locator
from Credentials import credentials
from ExpectedLinks import links, admin_login_page_url
import unittest


class AdminLoginPage(unittest.TestCase):
    """
    This Robot Library contains keywords operating on the admin_login_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, browser, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._browser = browser
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_admin_login_page(self):
        """
        Goes to Admin Login Page specified by admin_login_page_url. It waits until the page's login button is enabled.
        Once the login button is loaded, it checks title_text, username_text, password_text, and
        login_button_text for correctness.
        :return: None
        """
        self._loader.sl.go_to(url=admin_login_page_url)
        self._loader.sl.wait_until_element_is_enabled(locator=locator['admin_login_page']['login_button'])
        self._verify_texts_on_admin_login_page()

    def _verify_texts_on_admin_login_page(self):

        self._loader.sl.element_text_should_be(locator=locator['admin_login_page']['title'],
                                               expected=expected['admin_login_page']['title_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_login_page']['username_title'],
                                               expected=expected['admin_login_page']['username_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_login_page']['password_title'],
                                               expected=expected['admin_login_page']['password_text'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_login_page']['login_button'],
                                                          attribute='value',
                                                          expected=expected['admin_login_page']['login_button_text'])

    def enter_valid_admin_credentials_and_submit(self):
        """
        Logins as admin user via admin login page. If the login attempt is successful, user is redirected to
        admin main page. This test checks the success of the login attempt by waiting for 'logout' element
        in the main page. If the element is enabled, then the url of of the redirected page is checked against
        expected_admin_main_page_url. Then the test verifies all the texts and the links on the admin main page
        :return: None
        """
        self._loader.sl.input_text(locator=locator['admin_login_page']['username_field'],
                                   text=credentials['valid_admin']['username'])
        self._loader.sl.input_password(locator=locator['admin_login_page']['password_field'],
                                       password=credentials['valid_admin']['password'])
        self._loader.sl.click_element(locator=locator['admin_login_page']['login_button'])

    def click_on_add_group_button(self):
        """
        In admin_main_page, it clicks on add_group button, once redirected to the add_group_page
        :return None
        """
        self._loader.sl.click_link(locator=locator['admin_main_page']['add_group'])

