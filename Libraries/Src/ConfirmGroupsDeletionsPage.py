from LibraryLoader import LibraryLoader
from ExpectedTexts import expected
from ExpectedLinks import links, expected_groups_page_url, base_link
from Locators import locator


class ConfirmGroupsDeletionsPage:
    """
    This Robot Library contains keywords operating on the XXX
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._loader = LibraryLoader.get_instance()  # singleton

    def verify_confirm_group_deletions_page(self, group_name):
        self._loader.sl.wait_until_element_is_enabled(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline'])
        # at this stage, the page is assumed to be loaded
        # verify that confirm_groups_deletions_page url is correct
        observed_confirm_groups_deletions_page_url = self._loader.sl.get_location()
        assert expected_groups_page_url == observed_confirm_groups_deletions_page_url

        self._verify_texts_on_confirm_groups_deletions_page(group_name)
        self._verify_links_on_confirm_groups_deletions_page(group_name)

    def _verify_texts_on_confirm_groups_deletions_page(self, group_name):
        self._loader.sl.element_text_should_be(locator=locator['confirm_groups_deletions_page']['breadcrumbs'],
                                               expected=expected['confirm_groups_deletions_page']['breadcrumbs_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_headline_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_question'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_question_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['summary'],
            expected=expected['confirm_groups_deletions_page']['summary_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['objects'],
            expected=expected['confirm_groups_deletions_page']['objects_text'])

        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        self._loader.sl.element_text_should_be(
            locator=group_locator,
            expected=group_name)

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['confirm_deletion_button'],
            attribute='value',
            expected=expected['confirm_groups_deletions_page']['confirm_deletion_button_text'])

        self._loader.sl.element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
            expected=expected['confirm_groups_deletions_page']['cancel_deletion_button_text'])

    def _verify_links_on_confirm_groups_deletions_page(self, group_name):
        self._loader.sl.element_attribute_value_should_be(locator=locator['confirm_groups_deletions_page']['home'],
                                                          attribute='href',
                                                          expected=links['confirm_groups_deletions_page']['home_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['authentication_and_authorization'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['authentication_and_authorization_link'])

        self._loader.sl.element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['groups'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['groups_link'])

        # the group to be deleted shows as an item under locator['confirm_groups_deletions_page']['objects']
        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        group_link = self._loader.sl.get_element_attribute(locator=group_locator, attribute='href')
        # TODO: Do the below checks more efficiently with RegEx check when txt2re.com is up again
        assert base_link in group_link
        assert '/admin/auth/group/' in group_link
        assert '/change/' in group_link

        # cancel_deletion_button
        observed_cancel_deletion_button_link = self._loader.sl.get_element_attribute(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'], attribute='href')
        assert observed_cancel_deletion_button_link == \
            links['confirm_groups_deletions_page']['cancel_deletion_button_link']

    def press_confirm_button(self):
        self._loader.sl.click_element(locator=locator['confirm_groups_deletions_page']['confirm_deletion_button'])

