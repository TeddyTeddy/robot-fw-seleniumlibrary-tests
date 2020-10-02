import unittest
from mockito import expect, unstub, verify, verifyNoUnwantedInteractions
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from ConfirmGroupsDeletionsPage import ConfirmGroupsDeletionsPage     # class under test (CUT)
from ExpectedLinks import links, expected_groups_page_url, base_link
from ExpectedTexts import expected


class ConfirmGroupsDeletionsPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_test_verify_confirm_group_deletions_page(group_name):

        expect(LibraryLoader.get_instance().sl).wait_until_element_is_enabled(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline']
        ).thenReturn(None)
        # at this stage, the page is assumed to be loaded
        expect(LibraryLoader.get_instance().sl).get_location().thenReturn(expected_groups_page_url)

        # configure mock calls in _verify_texts_on_confirm_groups_deletions_page(group_name)
        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['breadcrumbs'],
            expected=expected['confirm_groups_deletions_page']['breadcrumbs_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_headline_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_question'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_question_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['summary'],
            expected=expected['confirm_groups_deletions_page']['summary_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['objects'],
            expected=expected['confirm_groups_deletions_page']['objects_text']
        ).thenReturn(None)

        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=group_locator,
            expected=group_name
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['confirm_deletion_button'],
            attribute='value',
            expected=expected['confirm_groups_deletions_page']['confirm_deletion_button_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
            expected=expected['confirm_groups_deletions_page']['cancel_deletion_button_text']
        ).thenReturn(None)

        # configure mock calls in _verify_links_on_confirm_groups_deletions_page(group_name)
        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['home'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['home_link']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['authentication_and_authorization'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['authentication_and_authorization_link']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['groups'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['groups_link']
        ).thenReturn(None)

        # the group to be deleted shows as an item under locator['confirm_groups_deletions_page']['objects']
        # https://glacial-earth-31542.herokuapp.com/admin/auth/group/79/change/
        url = f'{base_link}admin/auth/group/23/change/'
        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        expect(LibraryLoader.get_instance().sl).get_element_attribute(
            locator=group_locator, attribute='href'
        ).thenReturn(url)

        # cancel_deletion_button
        expect(LibraryLoader.get_instance().sl).get_element_attribute(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'], attribute='href'
        ).thenReturn(links['confirm_groups_deletions_page']['cancel_deletion_button_link'])

        # CUT gets magically the mock instances (i.e. _loader & sl)
        confirm_group_deletions_page = ConfirmGroupsDeletionsPage()

        # method under test gets called
        confirm_group_deletions_page.verify_confirm_group_deletions_page(group_name)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_verify_confirm_group_deletions_page(self):
        ConfirmGroupsDeletionsPageUT.do_test_verify_confirm_group_deletions_page(group_name='blog_editors')
        self.tearDown()

        self.setUp()
        ConfirmGroupsDeletionsPageUT.do_test_verify_confirm_group_deletions_page(group_name='group_editors')

    def test_press_confirm_button(self):
        # configure the mock selenium library for press_confirm_button()'s calls
        expect(LibraryLoader.get_instance().sl).click_element(
            locator=locator['confirm_groups_deletions_page']['confirm_deletion_button']
        ).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        confirm_group_deletions_page = ConfirmGroupsDeletionsPage()

        # method under test gets called
        confirm_group_deletions_page.press_confirm_button()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()


if __name__ == '__main__':
    unittest.main()
