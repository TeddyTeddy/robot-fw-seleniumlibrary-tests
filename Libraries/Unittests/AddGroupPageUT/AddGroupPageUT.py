import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from SeleniumLibraryStub import configure_mock_calls_in_verify_remove_all_permission_link
from SeleniumLibraryStub import configure_mock_calls_in_enter_name_for_new_group
from SeleniumLibraryStub import configure_mock_calls_in_enter_search_term_in_available_permissions_filter
from SeleniumLibraryStub import do_get_text_for_available_permissions_dropdown
from SeleniumLibraryStub import configure_mock_calls_in_clear_available_permissions_filter
from SeleniumLibraryStub import configure_mock_calls_in_click_on_save_button
from SeleniumLibraryStub import configure_mock_calls_in_choose_all_filtered_permissions
from SeleniumLibraryStub import configure_mock_calls_in_verify_add_group_page
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from AddGroupPage import AddGroupPage     # class under test (CUT)
from ExpectedLinks import expected_add_group_page_url, links
from ExpectedTexts import expected
from ExpectedAttributeValues import eav


class AddGroupPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_test_verify_add_group_page(chosen_permissions_dropdown_text):
        # configure the mock selenium library for verify_add_group_page()'s calls
        configure_mock_calls_in_verify_add_group_page(sl=LibraryLoader.get_instance().sl)
        configure_mock_calls_in_verify_remove_all_permission_link(
            LibraryLoader.get_instance().sl,
            chosen_permissions_dropdown_text=chosen_permissions_dropdown_text)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.verify_add_group_page()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        AddGroupPageUT.do_verify_mock_calls_in_verify_texts_on_add_group_page()
        AddGroupPageUT.do_verify_mock_calls_in_verify_links_on_add_group_page()
        AddGroupPageUT.do_verify_mock_calls_in_verify_remove_all_permission_link(
            chosen_permissions_dropdown_text=chosen_permissions_dropdown_text)
        AddGroupPageUT.do_verify_mock_calls_in_verify_the_buttons_on_add_group_page()

    @staticmethod
    def do_verify_mock_calls_in_verify_texts_on_add_group_page():
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['breadcrumbs'],
            expected=expected['add_group_page']['breadcrumbs_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['add_group'],
            expected=expected['add_group_page']['add_group_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['name'],
            expected=expected['add_group_page']['name_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['permissions'],
            expected=expected['add_group_page']['permissions_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['available_permissions_title'],
            expected=expected['add_group_page']['available_permissions_title_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['available_permissions_dropdown'],
            expected=expected['add_group_page']['available_permissions_dropdown_content']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['available_permissions_tooltip'],
            attribute='title',
            expected=expected['add_group_page']['available_permissions_tooltip_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['choose_all_permissions'],
            expected=expected['add_group_page']['choose_all_permissions_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['help_to_select_multiple_permissions'],
            expected=expected['add_group_page']['help_to_select_multiple_permissions_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['chosen_permissions_title'],
            expected=expected['add_group_page']['chosen_permissions_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['chosen_permissions_tooltip'],
            attribute='title',
            expected=expected['add_group_page']['chosen_permissions_tooltip_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['chosen_permissions_dropdown'],
            expected=expected['add_group_page']['chosen_permissions_dropdown_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['add_group_page']['remove_all_permissions_option'],
            expected=expected['add_group_page']['remove_all_permissions_text']
        )

    @staticmethod
    def do_verify_mock_calls_in_verify_links_on_add_group_page():
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['home_link'],
            attribute='href',
            expected=links['add_group_page']['home_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['authentication_and_authorization_link'],
            attribute='href',
            expected=links['add_group_page']['authentication_and_authorization_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['groups_link'],
            attribute='href',
            expected=links['add_group_page']['groups_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['choose_all_permissions_option'],
            attribute='href',
            expected=links['add_group_page']['choose_all_permissions_link']
        )

    @staticmethod
    def do_verify_mock_calls_in_verify_remove_all_permission_link(chosen_permissions_dropdown_text):
        verify(LibraryLoader.get_instance().sl, times=1).get_text(
            locator=locator['add_group_page']['chosen_permissions_dropdown']
        )

        if chosen_permissions_dropdown_text:
            verify(LibraryLoader.get_instance().sl, times=1).element_should_be_enabled(
                locator=locator['add_group_page']['remove_all_permissions_option']
            )

            verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
                locator=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                expected=eav['add_group_page']['remove_all_permissions_active']
            )

        else:
            # there are no permissions added to chosen_permissions_dropdown element
            verify(LibraryLoader.get_instance().sl, times=1).element_should_be_enabled(
                locator=locator['add_group_page']['remove_all_permissions_option']
            )

            verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
                locator=locator['add_group_page']['remove_all_permissions_option'],
                attribute='class',
                expected=eav['add_group_page']['remove_all_permissions_inactive']
            )

    @staticmethod
    def do_verify_mock_calls_in_verify_the_buttons_on_add_group_page():
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['save_and_add_another_button'],
            attribute='value',
            expected=expected['add_group_page']['save_and_add_another_button_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['save_and_continue_editing_button'],
            attribute='value',
            expected=expected['add_group_page']['save_and_continue_editing_button_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['add_group_page']['save_button'],
            attribute='value',
            expected=expected['add_group_page']['save_button_text']
        )
        
    def test_verify_add_group_page(self):
        # with permissions_drowdown_text is non empty string, "Remove all" button should be active
        AddGroupPageUT.do_test_verify_add_group_page(
            chosen_permissions_dropdown_text=expected['add_group_page']['auth-group-can_add_group'])
        self.tearDown()

        self.setUp()
        AddGroupPageUT.do_test_verify_add_group_page(chosen_permissions_dropdown_text='')

    def test_enter_name_for_new_group(self):
        # configure the mock selenium library for enter_name_for_new_group()'s calls
        group_name = 'blog_editors'
        configure_mock_calls_in_enter_name_for_new_group(
            sl=LibraryLoader.get_instance().sl,
            group_name=group_name
        )
        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.enter_name_for_new_group(group_name=group_name)

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).input_text(
            locator=locator['add_group_page']['input_name_field'],
            text=group_name
        )

    def test_enter_search_term_in_available_permissions_filter(self):
        self.do_test_enter_search_term_in_available_permissions_filter(permission_search_term='blog')
        self.tearDown()
        self.setUp()
        self.do_test_enter_search_term_in_available_permissions_filter(permission_search_term='yielding no permissions')

    def do_test_enter_search_term_in_available_permissions_filter(self, permission_search_term):
        configure_mock_calls_in_enter_search_term_in_available_permissions_filter(
            sl=LibraryLoader.get_instance().sl,
            permission_search_term=permission_search_term
        )
        dropdown_text = do_get_text_for_available_permissions_dropdown(permission_search_term)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        permissions_found = add_group_page.enter_search_term_in_available_permissions_filter(
            permission_search_term=permission_search_term
        )

        self.assertEqual(bool(dropdown_text), permissions_found)
        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).input_text(
            locator=locator['add_group_page']['input_permission_field'],
            text=permission_search_term
        )

        verify(LibraryLoader.get_instance().sl, times=1).get_text(
            locator=locator['add_group_page']['available_permissions_dropdown']
        )

    def test_choose_all_filtered_permissions(self):
        # configure the mock selenium library for choose_all_filtered_permissions()'s calls
        configure_mock_calls_in_choose_all_filtered_permissions(
            sl=LibraryLoader.get_instance().sl,
        )

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.choose_all_filtered_permissions()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).get_webelements(
            locator=locator['add_group_page']['generic_filtered_permission']
        )

        for element in LibraryLoader.get_instance().sl.filtered_permission_elements:
            verify(LibraryLoader.get_instance().sl, times=1).get_text(element)
            verify(LibraryLoader.get_instance().sl, times=1).press_keys(element, 'CTRL')

        verify(LibraryLoader.get_instance().sl, times=1).click_link(
            locator=locator['add_group_page']['choose_all_permissions_option']
        )

        # refer to_configure_mock_calls_in_verify_permissions_added(sl)
        verify(LibraryLoader.get_instance().sl, times=1).get_webelements(
            locator=locator['add_group_page']['generic_chosen_permission']
        )

        for element in LibraryLoader.get_instance().sl.chosen_permission_elements:
            verify(LibraryLoader.get_instance().sl, times=1).get_text(element)

    def test_clear_available_permissions_filter(self):
        # configure the mock selenium library for clear_available_permissions_filter()'s calls
        configure_mock_calls_in_clear_available_permissions_filter(LibraryLoader.get_instance().sl)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.clear_available_permissions_filter()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).clear_element_text(
            locator=locator['add_group_page']['input_permission_field']
        )

    def test_click_on_save_button(self):
        # configure the mock selenium library for click_on_save_button()'s calls
        configure_mock_calls_in_click_on_save_button(LibraryLoader.get_instance().sl)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        add_group_page = AddGroupPage()

        # method under test gets called
        add_group_page.click_on_save_button()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).click_element(
            locator=locator['add_group_page']['save_button']
        )


if __name__ == '__main__':
    unittest.main()
