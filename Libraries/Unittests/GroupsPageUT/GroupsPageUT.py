import unittest
from mockito import unstub, verify
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from SeleniumLibraryStub import configure_mock_calls_in_verify_groups_page_loaded
from SeleniumLibraryStub import configure_mock_calls_in_verify_group_added
from SeleniumLibraryStub import configure_mock_calls_in_select_checkbox_for_group
from Locators import locator
from GroupsPage import GroupsPage     # class under test (CUT)
from ExpectedLinks import links, base_link
from ExpectedTexts import expected


class GroupsPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        pass

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_verify_mock_calls_in_verify_texts_on_groups_page(group_name):
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['breadcrumbs'],
            expected=expected['groups_page']['breadcrumbs_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['home_link'],
            expected=expected['groups_page']['home_link_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            expected=expected['groups_page']['authentication_and_authorization_link_text']
        )

        GroupsPageUT.do_verify_mock_calls_in_verify_dynamic_text_group_x_added_successfully(group_name)

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['select_group_to_change'],
            expected=expected['groups_page']['select_group_to_change_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['groups_page']['search_button'],
            attribute='value',
            expected=expected['groups_page']['search_button_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['action'],
            expected=expected['groups_page']['action_text']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['delete_selected_groups_option'],
            expected=expected['groups_page']['delete_selected_groups_option_text']
        )

        GroupsPageUT.do_verify_mock_calls_in_verify_dynamic_text_x_of_y_selected()

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['select_all_groups'],
            expected=expected['groups_page']['select_all_groups_text']
        )

    @staticmethod
    def do_verify_mock_calls_in_verify_dynamic_text_x_of_y_selected():
        verify(LibraryLoader.get_instance().sl, times=1).get_text(locator=locator['groups_page']['x_of_y_selected'])
        verify(LibraryLoader.get_instance().sl, times=1).get_text(locator=locator['groups_page']['y_groups'])

    @staticmethod
    def do_verify_mock_calls_in_verify_dynamic_text_group_x_added_successfully(group_name):
        group_x_added_successfully_text = expected['groups_page']['group_x_added_successfully_text'] % group_name

        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator['groups_page']['group_x_added_successfully'],
            expected=group_x_added_successfully_text
        )

    @staticmethod
    def do_verify_mock_calls_in_verify_links_on_groups_page(group_name):
        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['groups_page']['home_link'],
            attribute='href',
            expected=links['groups_page']['home_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            attribute='href',
            expected=links['groups_page']['authentication_and_authorization_link']
        )

        verify(LibraryLoader.get_instance().sl, times=1).element_attribute_value_should_be(
            locator=locator['groups_page']['add_group'],
            attribute='href',
            expected=links['groups_page']['add_group_link']
        )

        GroupsPageUT.do_verify_mock_calls_in_verify_dynamic_link_for_group_name(group_name)

    @staticmethod
    def do_verify_mock_calls_in_verify_dynamic_link_for_group_name(group_name):
        url = f'{base_link}/admin/auth/group/23/change/'
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        verify(LibraryLoader.get_instance().sl, times=1).get_element_attribute(
            locator=locator_formatter,
            attribute='href')

    @staticmethod
    def do_test_verify_groups_page_loaded(group_name):
        # configure the mock selenium library for verify_groups_page_loaded()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='verify_groups_page_loaded')
        configure_mock_calls_in_verify_groups_page_loaded(
            sl=LibraryLoader.get_instance().sl,
            group_name=group_name
        )
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.verify_groups_page_loaded(group_name)

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).wait_until_element_is_enabled(
            locator=locator['groups_page']['select_group_to_change']
        )
        # groups_page is loaded at this point
        # verify that groups_page url is correct
        verify(LibraryLoader.get_instance().sl, times=1).get_location()
        GroupsPageUT.do_verify_mock_calls_in_verify_texts_on_groups_page(group_name)
        GroupsPageUT.do_verify_mock_calls_in_verify_links_on_groups_page(group_name)

    def test_verify_groups_page_loaded(self):
        GroupsPageUT.do_test_verify_groups_page_loaded(group_name='blog_editors')
        GroupsPageUT.do_test_verify_groups_page_loaded(group_name='group_editors')

    @staticmethod
    def do_test_verify_group_added(group_name):
        # configure the mock selenium library for verify_group_added()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='verify_group_added')
        configure_mock_calls_in_verify_group_added(
            sl=LibraryLoader.get_instance().sl,
            group_name=group_name
        )
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.verify_group_added(group_name)

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        verify(LibraryLoader.get_instance().sl, times=1).element_text_should_be(
            locator=locator_formatter,
            expected=group_name
        )

    def test_verify_group_added(self):
        GroupsPageUT.do_test_verify_group_added(group_name='blog_editors')
        GroupsPageUT.do_test_verify_group_added(group_name='group_editors')
        GroupsPageUT.do_test_verify_group_added(group_name='')


    @staticmethod
    def do_test_select_checkbox_for_group(group_name):
        # configure the mock selenium library for select_checkbox_for_group()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='select_checkbox_for_group')
        configure_mock_calls_in_select_checkbox_for_group(
            sl=LibraryLoader.get_instance().sl,
            group_name=group_name
        )
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.select_checkbox_for_group(group_name)

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        group_element_checkbox_locator = locator['groups_page']['generic_group_element_checkbox'] % group_name
        verify(LibraryLoader.get_instance().sl, times=1).click_element(locator=group_element_checkbox_locator)

    def test_select_checkbox_for_group(self):
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='blog_editors')
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='group_editors')
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='')

    def test_select_delete_selected_groups_dropdown(self):
        # configure the mock selenium library for select_delete_selected_groups_dropdown()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='select_delete_selected_groups_dropdown')
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.select_delete_selected_groups_dropdown()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).click_element(
            locator=locator['groups_page']['delete_selected_groups_option']
        )

    def test_press_go(self):
        # configure the mock selenium library for select_delete_selected_groups_dropdown()'s calls
        LibraryLoaderStub.configure_mock_library_loader(method_under_test='press_go')
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.press_go()

        # verify that correct mock instance sl got called with correct instance methods with correct arguments
        verify(LibraryLoader.get_instance().sl, times=1).click_element(locator=locator['groups_page']['go_button'])


if __name__ == '__main__':
    unittest.main()
