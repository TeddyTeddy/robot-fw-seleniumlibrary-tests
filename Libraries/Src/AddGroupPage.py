from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_add_group_page_url
from ExpectedAttributeValues import eav
from Locators import locator
from robot.api import logger


class AddGroupPage:
    """
    This Robot Library contains keywords operating on the expected_admin_main_page_url
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_add_group_page(self):
        """
        In admin_main_page, it clicks on add_group button, once redirected to the add_group_page.
        Once redirection occurs, this method checks for element title to be visible on add_group_page.
        Then it verifies that current url is expected_add_group_page_url
        It then verifies the page's texts and the links for correctness
        :return: None
        """
        # wait until title element is visible on add_group_page
        self._loader.sl.wait_until_element_is_visible(locator=locator['add_group_page']['title'])

        # check the validity of the url on the add_group_page
        observed_add_group_page_url = self._loader.sl.get_location()
        assert observed_add_group_page_url == expected_add_group_page_url

        # at this point, the add_group_page is loaded
        self._verify_texts_on_add_group_page()
        self._verify_links_on_add_group_page()
        self._verify_the_buttons_on_add_group_page()

    def _verify_the_buttons_on_add_group_page(self):
        """
        Verifies the correctness of the value attribute in the following buttons:
            save_and_add_another_button
            save_and_continue_editing_button
            save_button
        :return: None
        """
        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['save_and_add_another_button'],
            attribute='value',
            expected=expected['add_group_page']['save_and_add_another_button_text'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['save_and_continue_editing_button'],
            attribute='value',
            expected=expected['add_group_page']['save_and_continue_editing_button_text'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['save_button'],
            attribute='value',
            expected=expected['add_group_page']['save_button_text'])

    def _verify_texts_on_add_group_page(self):
        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['breadcrumbs'],
                                               expected=expected['add_group_page']['breadcrumbs_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['add_group'],
                                               expected=expected['add_group_page']['add_group_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['name'],
                                               expected=expected['add_group_page']['name_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['permissions'],
                                               expected=expected['add_group_page']['permissions_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['available_permissions_title'],
                                               expected=expected['add_group_page']['available_permissions_title_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['available_permissions_dropdown'],
                                               expected=expected['add_group_page']['available_permissions_dropdown_content'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['available_permissions_tooltip'],
            attribute='title',
            expected=expected['add_group_page']['available_permissions_tooltip_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['choose_all_permissions'],
                                               expected=expected['add_group_page']['choose_all_permissions_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['help_to_select_multiple_permissions'],
                                               expected=expected['add_group_page']['help_to_select_multiple_permissions_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['chosen_permissions_title'],
                                               expected=expected['add_group_page']['chosen_permissions_text'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['chosen_permissions_tooltip'],
            attribute='title',
            expected=expected['add_group_page']['chosen_permissions_tooltip_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['chosen_permissions_dropdown'],
                                               expected=expected['add_group_page']['chosen_permissions_dropdown_text'])

        self._loader.sl.element_text_should_be(locator=locator['add_group_page']['remove_all_permissions_option'],
                                               expected=expected['add_group_page']['remove_all_permissions_text'])

    def _verify_links_on_add_group_page(self):
        """
        Verify all the links on add_groups_page on expected_add_group_page_url
        :return: None
        """
        self._loader.sl.element_attribute_value_should_be(locator=locator['add_group_page']['home_link'],
                                                          attribute='href',
                                                          expected=links['add_group_page']['home_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['authentication_and_authorization_link'],
            attribute='href',
            expected=links['add_group_page']['authentication_and_authorization_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['groups_link'],
            attribute='href',
            expected=links['add_group_page']['groups_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['add_group_page']['choose_all_permissions_option'],
            attribute='href',
            expected=links['add_group_page']['choose_all_permissions_link'])

        self._verify_remove_all_permission_link()

    def _verify_remove_all_permission_link(self):
        """
        If there are no permissions added under chosen_permissions_dropdown element,
        then remove_all_permissions_option should not be active.
        Otherwise (there are permissions added under chosen_permissions_dropdown element),
        then remove_all_permissions_option should have the right class attribute and should be active.
        :return: None
        """
        if self._loader.sl.get_text(locator=locator['add_group_page']['chosen_permissions_dropdown']):
            self._loader.sl.element_should_be_enabled(
                locator=locator['add_group_page']['remove_all_permissions_option'])

            self._loader.sl.element_attribute_value_should_be(
                locator=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                expected=eav['add_group_page']['remove_all_permissions_active'])

        else:
            # there are no permissions added to chosen_permissions_dropdown element
            # TODO: Why the element should be enabled?
            self._loader.sl.element_should_be_enabled(
                locator=locator['add_group_page']['remove_all_permissions_option'])

            self._loader.sl.element_attribute_value_should_be(
                locator=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                expected=eav['add_group_page']['remove_all_permissions_inactive'])

    def enter_name_for_new_group(self, group_name):
        self._loader.sl.input_text(locator=locator['add_group_page']['input_name_field'],
                                   text=group_name)

    def enter_search_term_in_available_permissions_filter(self, permission_search_term):
        self._loader.sl.input_text(locator=locator['add_group_page']['input_permission_field'],
                                   text=permission_search_term)
        # return True if there are permissions listed, otherwise return False
        return bool(self._loader.sl.get_text(locator=locator['add_group_page']['available_permissions_dropdown']))

    def choose_all_filtered_permissions(self):
        """
        Given that a search term is entered into input_permission_field, the available_permissions_dropdown
        lists filtered permissions. This method creates a list of all the filtered permissions. Then it selects
        each and every element in filtered_permissions_elements. Then it clicks
        on choose_all_permissions_option. It then verifies that the permissions are added inside
        chosen_permissions_dropdown.
        :return: None
        """
        # create a list of all the permissions listed inside available_permissions_dropdown
        filtered_permission_elements = self._loader.sl.get_webelements(locator=locator['add_group_page']['generic_filtered_permission'])
        filtered_permissions = []
        for element in filtered_permission_elements:
            permission = self._loader.sl.get_text(element)
            filtered_permissions.append(permission)
        logger.info(filtered_permissions)

        # then select each and every element in filtered_permission_elements by pressing CTRL key and clicking on them
        for element in filtered_permission_elements:
            self._loader.sl.press_keys(element, 'CTRL')

        # Then it clicks on choose_all_permissions_option
        self._loader.sl.click_link(locator=locator['add_group_page']['choose_all_permissions_option'])
        # It then verifies that the permissions are added inside chosen_permissions_dropdown.
        self._verify_permissions_added(filtered_permissions)

    def _verify_permissions_added(self, filtered_permissions):  # use set operations like set1.contains(set2)
        """
        Verifies that filtered_permissions is found under chosen_permissions_dropdown. Fails with assert otherwise.
        :param filtered_permissions: a list of filtered & chosen permissions to be verified to be added inside
        chosen_permissions_dropdown as generic_chosen_permission
        :return:
        """
        chosen_permission_elements = self._loader.sl.get_webelements(
            locator=locator['add_group_page']['generic_chosen_permission'])
        chosen_permissions = []
        for element in chosen_permission_elements:
            permission = self._loader.sl.get_text(element)
            chosen_permissions.append(permission)
        chosen_permissions = set(chosen_permissions)
        filtered_permissions = set(filtered_permissions)
        logger.info(chosen_permissions)
        logger.info(filtered_permissions)
        # NOTE: sorted(chosen_permissions) == sorted(filtered_permissions) does not work.
        # Why? because chosen_permissions is a larger set
        assert chosen_permissions.issuperset(filtered_permissions)

    def clear_available_permissions_filter(self):
        self._loader.sl.clear_element_text(locator=locator['add_group_page']['input_permission_field'])

    def click_on_save_button(self):
        self._loader.sl.click_element(locator=locator['add_group_page']['save_button'])

