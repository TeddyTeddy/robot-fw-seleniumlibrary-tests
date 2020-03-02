import unittest
from mockito import unstub, verify, verifyNoUnwantedInteractions, expect
from LibraryLoader import LibraryLoader
import LibraryLoaderStub
from Locators import locator
from GroupsPage import GroupsPage     # class under test (CUT)
from ExpectedLinks import links, expected_groups_page_url, base_link
from ExpectedTexts import expected


class GroupsPageUT(unittest.TestCase):
    def setUp(self) -> None:  # before running an individual test case
        # instantiate a mock LibraryLoader, which returns a mock sl
        LibraryLoaderStub.configure_mock_library_loader()

    def tearDown(self) -> None:  # after running an individual test case
        unstub()

    @staticmethod
    def do_test_verify_groups_page_loaded(group_name):
        # configure the mock selenium library for verify_groups_page_loaded()'s calls
        expect(LibraryLoader.get_instance().sl).wait_until_element_is_enabled(
            locator=locator['groups_page']['select_group_to_change']
        ).thenReturn(None)
        # groups_page is loaded at this point
        expect(LibraryLoader.get_instance().sl).get_location().thenReturn(expected_groups_page_url)

        # configure mock calls in _verify_texts_on_groups_page(group_name)
        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['breadcrumbs'],
            expected=expected['groups_page']['breadcrumbs_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['home_link'],
            expected=expected['groups_page']['home_link_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            expected=expected['groups_page']['authentication_and_authorization_link_text']
        ).thenReturn(None)

        # configure mock calls in _verify_dynamic_text_group_x_added_successfully(group_name)
        group_x_added_successfully_text = expected['groups_page']['group_x_added_successfully_text'] % group_name
        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['group_x_added_successfully'],
            expected=group_x_added_successfully_text
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['select_group_to_change'],
            expected=expected['groups_page']['select_group_to_change_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['groups_page']['search_button'],
            attribute='value',
            expected=expected['groups_page']['search_button_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['action'],
            expected=expected['groups_page']['action_text']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['delete_selected_groups_option'],
            expected=expected['groups_page']['delete_selected_groups_option_text']
        ).thenReturn(None)

        # configure mock calls in _verify_dynamic_text_x_of_y_selected()
        expect(LibraryLoader.get_instance().sl).get_text(locator=locator['groups_page']['x_of_y_selected']).thenReturn('0 of 5 selected')
        expect(LibraryLoader.get_instance().sl).get_text(locator=locator['groups_page']['y_groups']).thenReturn('5 groups')

        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator['groups_page']['select_all_groups'],
            expected=expected['groups_page']['select_all_groups_text']
        ).thenReturn(None)

        # configure mock calls in _verify_links_on_groups_page(group_name)
        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['groups_page']['home_link'],
            attribute='href',
            expected=links['groups_page']['home_link']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['groups_page']['authentication_and_authorization_link'],
            attribute='href',
            expected=links['groups_page']['authentication_and_authorization_link']
        ).thenReturn(None)

        expect(LibraryLoader.get_instance().sl).element_attribute_value_should_be(
            locator=locator['groups_page']['add_group'],
            attribute='href',
            expected=links['groups_page']['add_group_link']
        ).thenReturn(None)

        # configure mock calls _in_verify_dynamic_link_for_group_name(group_name)
        url = f'{base_link}/admin/auth/group/23/change/'
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        expect(LibraryLoader.get_instance().sl).get_element_attribute(
            locator=locator_formatter,
            attribute='href').thenReturn(url)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.verify_groups_page_loaded(group_name)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_verify_groups_page_loaded(self):
        GroupsPageUT.do_test_verify_groups_page_loaded(group_name='blog_editors')
        self.tearDown()

        self.setUp()
        GroupsPageUT.do_test_verify_groups_page_loaded(group_name='group_editors')

    @staticmethod
    def do_test_verify_group_added(group_name):
        # configure the mock selenium library for verify_group_added()'s calls
        locator_formatter = locator['groups_page']['generic_group_element'] % group_name
        expect(LibraryLoader.get_instance().sl).element_text_should_be(
            locator=locator_formatter,
            expected=group_name
        ).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.verify_group_added(group_name)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_verify_group_added(self):
        GroupsPageUT.do_test_verify_group_added(group_name='blog_editors')
        self.tearDown()
        self.setUp()
        GroupsPageUT.do_test_verify_group_added(group_name='group_editors')
        self.tearDown()
        self.setUp()
        GroupsPageUT.do_test_verify_group_added(group_name='')

    @staticmethod
    def do_test_select_checkbox_for_group(group_name):
        # configure the mock selenium library for select_checkbox_for_group()'s calls
        group_element_checkbox_locator = locator['groups_page']['generic_group_element_checkbox'] % group_name
        expect(LibraryLoader.get_instance().sl).click_element(locator=group_element_checkbox_locator).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.select_checkbox_for_group(group_name)

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_select_checkbox_for_group(self):
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='blog_editors')
        self.tearDown()
        self.setUp()
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='group_editors')
        self.tearDown()
        self.setUp()
        GroupsPageUT.do_test_select_checkbox_for_group(group_name='')

    def test_select_delete_selected_groups_dropdown(self):
        # configure the mock selenium library for select_delete_selected_groups_dropdown()'s calls
        expect(LibraryLoader.get_instance().sl).click_element(
            locator=locator['groups_page']['delete_selected_groups_option']
        ).thenReturn(None)
        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.select_delete_selected_groups_dropdown()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()

    def test_press_go(self):
        # configure the mock selenium library for select_delete_selected_groups_dropdown()'s calls
        expect(LibraryLoader.get_instance().sl).click_element(
            locator=locator['groups_page']['go_button']
        ).thenReturn(None)

        # CUT gets magically the mock instances (i.e. _loader & sl)
        groups_page = GroupsPage()

        # method under test gets called
        groups_page.press_go()

        # Verifies that expectations set via expect are met
        # all registered objects will be checked.
        verifyNoUnwantedInteractions()


if __name__ == '__main__':
    unittest.main()
