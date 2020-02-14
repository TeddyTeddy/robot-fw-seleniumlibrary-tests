import unittest
from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_admin_main_page_url
from Credentials import credentials
from Locators import number_of_add_buttons, number_of_change_buttons, locator
from robot.api import logger


class AdminMainPage(unittest.TestCase):
    """
    This Robot Library contains keywords operating on the expected_admin_main_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._loader = LibraryLoader.get_instance()  # singleton

    def go_to_admin_main_page(self):
        self._loader.sl.go_to(expected_admin_main_page_url)

    def verify_admin_main_page(self):
        """
        If the login attempt is successful, user is redirected to admin main page. This test checks the success
        of the login attempt by waiting for 'logout' element in the admin main page.
        If the element is enabled, then the url of of the redirected page is checked against
        expected_admin_main_page_url. Then the test verifies all the texts and the links on the admin main page
        :return: None
        """
        # at this stage, we expect a redirection to expected_admin_main_page_url
        # wait until the Logout Element is enabled on the page
        self._loader.sl.wait_until_element_is_enabled(locator=locator['admin_main_page']['logout'])
        # check the validity of the url on the admin_main_page page
        observed_admin_main_page_url = self._loader.sl.get_location()
        self.assertEqual(expected_admin_main_page_url, observed_admin_main_page_url)

        # admin_main_page is loaded at this point
        self._verify_texts_on_admin_main_page()
        self._verify_links_on_admin_main_page()

    def _verify_links_on_admin_main_page(self):
        """
        Verify all the links on admin_main_page on expected_admin_main_page_url
        :return: None
        """
        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['main_title'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['main_title_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['view_site'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['view_site_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['change_password'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['change_password_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['logout'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['logout_link'])

        # authentication and authorization section
        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['authentication_and_authorization'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['authentication_and_authorization_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['groups'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['groups_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['users'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['users_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['add_group'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['add_group_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['change_group'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['change_group_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['add_user'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['add_user_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['change_user'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['change_user_link'])
        # postings section
        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['postings'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['postings_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['blog_posts'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['blog_posts_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['add_blog_post'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['add_blog_post_link'])

        self._loader.sl.element_attribute_value_should_be(locator=locator['admin_main_page']['change_blog_post'],
                                                          attribute='href',
                                                          expected=links['admin_main_page']['change_blog_post_link'])

    def _verify_texts_on_admin_main_page(self):
        """
        Verify all the texts on admin_main_page on expected_admin_main_page_url
        :return: None
        """
        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['main_title'],
                                                 expected=expected['admin_main_page']['main_title_text'])

        # user navigation bar on the upper right of the page
        dynamic_user_tab_text = f"WELCOME, {credentials['valid_admin']['username'].upper()}. VIEW SITE / CHANGE PASSWORD / LOG OUT"
        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['welcome_user_x'],
                                               expected=dynamic_user_tab_text)

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['view_site'],
                                               expected=expected['admin_main_page']['view_site_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['change_password'],
                                               expected=expected['admin_main_page']['change_password_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['logout'],
                                               expected=expected['admin_main_page']['logout_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['site_administration'],
                                               expected=expected['admin_main_page']['site_administration_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['admin_main_page']['authentication_and_authorization'],
            expected=expected['admin_main_page']['authentication_and_authorization_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['groups'],
                                               expected=expected['admin_main_page']['groups_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['users'],
                                               expected=expected['admin_main_page']['users_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['postings'],
                                               expected=expected['admin_main_page']['postings_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['blog_posts'],
                                               expected=expected['admin_main_page']['blog_posts_text'])

        # the number of 'Add' buttons must be number_of_add_buttons
        logger.info(f"looking for Add buttons with XPATH = {locator['admin_main_page']['add_button']}")
        self._loader.sl.page_should_contain_element(locator=locator['admin_main_page']['add_button'],
                                                    limit=number_of_add_buttons)
        # the number of 'Change' buttons must be number_of_change_buttons
        logger.info(f"looking for Change buttons with XPATH = {locator['admin_main_page']['change_button']}")
        self._loader.sl.page_should_contain_element(locator=locator['admin_main_page']['change_button'],
                                                    limit=number_of_change_buttons)

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['recent_actions'],
                                               expected=expected['admin_main_page']['recent_actions_text'])

        self._loader.sl.element_text_should_be(locator=locator['admin_main_page']['my_actions'],
                                               expected=expected['admin_main_page']['my_actions_text'])


