from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_groups_page_url, base_link
from ExpectedAttributeValues import eav
from Locators import locator
from robot.api import logger
import re


class GroupsPage:
    """
    This Robot Library contains keywords operating on the XXX
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_groups_page_loaded(self, group_name):

        self._loader.sl.wait_until_element_is_enabled(locator=locator['groups_page']['select_group_to_change'])
        # groups_page is loaded at this point
        # verify that groups_page url is correct
        observed_groups_page_url = self._loader.sl.get_location()
        assert expected_groups_page_url == observed_groups_page_url

        self._verify_texts_on_groups_page(group_name)
        self._verify_links_on_groups_page(group_name)

    def _verify_texts_on_groups_page(self, group_name):
        self._loader.sl.element_text_should_be(locator=locator['groups_page']['breadcrumbs'],
                                               expected=expected['groups_page']['breadcrumbs_text'])

        self._loader.sl.element_text_should_be(locator=locator['groups_page']['home_link'],
                                               expected=expected['groups_page']['home_link_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            expected=expected['groups_page']['authentication_and_authorization_link_text'])

        self._verify_dynamic_text_group_x_added_successfully(group_name)

        self._loader.sl.element_text_should_be(locator=locator['groups_page']['select_group_to_change'],
                                               expected=expected['groups_page']['select_group_to_change_text'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['groups_page']['search_button'],
            attribute='value',
            expected=expected['groups_page']['search_button_text'])

        self._loader.sl.element_text_should_be(locator=locator['groups_page']['action'],
                                               expected=expected['groups_page']['action_text'])

        self._loader.sl.element_text_should_be(locator=locator['groups_page']['delete_selected_groups_option'],
                                               expected=expected['groups_page']['delete_selected_groups_option_text'])

        self._verify_dynamic_text_x_of_y_selected()

        self._loader.sl.element_text_should_be(locator=locator['groups_page']['select_all_groups'],
                                               expected=expected['groups_page']['select_all_groups_text'])

    def _verify_dynamic_text_group_x_added_successfully(self, group_name):
        group_x_added_successfully_text = expected['groups_page']['group_x_added_successfully_text'] % group_name

        self._loader.sl.element_text_should_be(
            locator=locator['groups_page']['group_x_added_successfully'],
            expected=group_x_added_successfully_text)

    def _verify_dynamic_text_x_of_y_selected(self):
        """x and y are dynamic numbers that are present in the following elements in groups_page:
                x_of_y_selected
                y_groups
           This method grabs y from y_groups element and then checks if y is in present in x_of_y_selected.
           If y is present, then assertion passes, otherwise assertion fails
           :return None
        """
        observed_x_of_y_selected = self._loader.sl.get_text(locator=locator['groups_page']['x_of_y_selected'])
        observed_y_groups = self._loader.sl.get_text(locator=locator['groups_page']['y_groups'])
        y = re.match('\\d+', observed_y_groups).group()
        logger.info(f'Observed {y} groups')
        assert y in observed_x_of_y_selected

    def _verify_links_on_groups_page(self, group_name):
        self._loader.sl.element_attribute_value_should_be(locator=locator['groups_page']['home_link'],
                                                          attribute='href',
                                                          expected=links['groups_page']['home_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            attribute='href',
            expected=links['groups_page']['authentication_and_authorization_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['groups_page']['add_group'],
            attribute='href',
            expected=links['groups_page']['add_group_link'])

        self._verify_dynamic_link_for_group_name(group_name)

    def _verify_dynamic_link_for_group_name(self, group_name):
        """
        An group element with text group_name is added in groups_page. This method checks that
        the element (which is an anchor with a dynamic href), contains the correct link
        :param group_name: the name of the group added to the group page (i.e. 'blog_editors')
        :return: None
        """
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        group_link = self._loader.sl.get_element_attribute(locator=locator_formatter, attribute='href')
        # TODO: Do the below checks more efficiently with RegEx check when txt2re.com is up again
        assert base_link in group_link
        assert '/admin/auth/group/' in group_link
        assert '/change/' in group_link

    def verify_group_added(self, group_name):
        # https://stackoverflow.com/questions/4302166/format-string-dynamically
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        self._loader.sl.element_text_should_be(locator=locator_formatter,
                                               expected=group_name)

    def select_checkbox_for_group(self, group_name):
        group_element_checkbox_locator = locator['groups_page']['generic_group_element_checkbox'] % group_name
        self._loader.sl.click_element(locator=group_element_checkbox_locator)

    def select_delete_selected_groups_dropdown(self):
        self._loader.sl.click_element(locator=locator['groups_page']['delete_selected_groups_option'])

    def press_go(self):
        self._loader.sl.click_element(locator=locator['groups_page']['go_button'])
