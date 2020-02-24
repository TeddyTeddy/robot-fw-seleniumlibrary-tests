import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from ConfirmGroupsDeletionsPage import ConfirmGroupsDeletionsPage     # class under test (CUT)
from SeleniumLibraryStub import configure_mock_calls_in_go_to_admin_main_page
from SeleniumLibraryStub import configure_mock_calls_in_press_confirm_button
from ExpectedLinks import links
from ExpectedTexts import expected


class ConfirmGroupsDeletionsPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_test_verify_confirm_group_deletions_page(group_name):
        # configure the mock selenium library for verify_confirm_group_deletions_page()'s calls
        configure_mock_calls_in_go_to_admin_main_page(
            sl=LibraryLoader.get_instance().sl,
            group_name=group_name
        )
        # CUT gets magically the mock instances (i.e. _loader & sl)
        confirm_group_deletions_page = ConfirmGroupsDeletionsPage()

        # method under test gets called
        confirm_group_deletions_page.verify_confirm_group_deletions_page(group_name)

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).wait_until_element_is_enabled(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline']
        )
        # at this stage, the page is assumed to be loaded
        # verify that confirm_groups_deletions_page url is correct
        verify(LibraryLoader.get_instance().sl, times=1).get_location()
        ConfirmGroupsDeletionsPageUT._verify_mock_calls_in_verify_texts_on_confirm_groups_deletions_page(group_name)
        ConfirmGroupsDeletionsPageUT._verify_mock_calls_in_verify_links_on_confirm_groups_deletions_page(group_name)

    @staticmethod
    def _verify_mock_calls_in_verify_texts_on_confirm_groups_deletions_page(group_name):
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['breadcrumbs'],
            expected=expected['confirm_groups_deletions_page']['breadcrumbs_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_headline'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_headline_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['are_you_sure_question'],
            expected=expected['confirm_groups_deletions_page']['are_you_sure_question_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['summary'],
            expected=expected['confirm_groups_deletions_page']['summary_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['objects'],
            expected=expected['confirm_groups_deletions_page']['objects_text']
        )

        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=group_locator,
            expected=group_name
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['confirm_deletion_button'],
            attribute='value',
            expected=expected['confirm_groups_deletions_page']['confirm_deletion_button_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
            expected=expected['confirm_groups_deletions_page']['cancel_deletion_button_text']
        )

    @staticmethod
    def _verify_mock_calls_in_verify_links_on_confirm_groups_deletions_page(group_name):
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['home'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['home_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['authentication_and_authorization'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['authentication_and_authorization_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['confirm_groups_deletions_page']['groups'],
            attribute='href',
            expected=links['confirm_groups_deletions_page']['groups_link']
        )

        # the group to be deleted shows as an item under locator['confirm_groups_deletions_page']['objects']
        group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
        verify(LibraryLoader.get_instance().sl, times=1).get_element_attribute(
            locator=group_locator, attribute='href'
        )

        # cancel_deletion_button
        verify(LibraryLoader.get_instance().sl, times=1).get_element_attribute(
            locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
            attribute='href'
        )

    def test_verify_confirm_group_deletions_page(self):
        ConfirmGroupsDeletionsPageUT.do_test_verify_confirm_group_deletions_page(group_name='blog_editors')
        self.tearDown()

        self.setUp()
        ConfirmGroupsDeletionsPageUT.do_test_verify_confirm_group_deletions_page(group_name='group_editors')

    def test_press_confirm_button(self):
        # configure the mock selenium library for press_confirm_button()'s calls
        configure_mock_calls_in_press_confirm_button(sl=LibraryLoader.get_instance().sl)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        confirm_group_deletions_page = ConfirmGroupsDeletionsPage()

        # method under test gets called
        confirm_group_deletions_page.press_confirm_button()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).click_element(
            locator=locator['confirm_groups_deletions_page']['confirm_deletion_button']
        )


if __name__ == '__main__':
    unittest.main()
