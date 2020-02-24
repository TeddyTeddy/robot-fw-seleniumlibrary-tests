from mockito import mock, when
from Credentials import DICT__CREDENTIALS
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from ExpectedLinks import expected_add_group_page_url, links
from ExpectedTexts import expected
from ExpectedAttributeValues import eav


def configure_mock_calls_in_click_on_save_button(sl):
    when(sl).click_element(locator=locator['add_group_page']['save_button']).thenReturn(None)


def configure_mock_calls_in_clear_available_permissions_filter(sl):
    when(sl).clear_element_text(locator=locator['add_group_page']['input_permission_field']).thenReturn(None)


def configure_mock_calls_in_choose_all_filtered_permissions(sl):
    sl.filtered_permission_elements = _get_filtered_permission_elements()

    when(sl).get_webelements(
        locator=locator['add_group_page']['generic_filtered_permission']
    ).thenReturn(sl.filtered_permission_elements)

    for element in sl.filtered_permission_elements:
        when(sl).get_text(element).thenReturn(element.text)
        when(sl).press_keys(element, 'CTRL').thenReturn(None)

    when(sl).click_link(locator=locator['add_group_page']['choose_all_permissions_option']).thenReturn(None)
    _configure_mock_calls_in_verify_permissions_added(sl)


def _get_filtered_permission_elements():
    element_one = mock()
    element_one.text = expected['add_group_page']['auth-user-can_add_user']

    element_two = mock()
    element_two.text = expected['add_group_page']['auth-user-can_change_user']

    element_three = mock()
    element_three.text = expected['add_group_page']['auth-user-can_delete_user']

    return [element_one, element_two, element_three]


def _configure_mock_calls_in_verify_permissions_added(sl):
    sl.chosen_permission_elements = _get_filtered_permission_elements()
    when(sl).get_webelements(
        locator=locator['add_group_page']['generic_chosen_permission']
    ).thenReturn(sl.chosen_permission_elements)

    for element in sl.chosen_permission_elements:
        when(sl).get_text(element).thenReturn(element.text)


def configure_mock_calls_in_enter_search_term_in_available_permissions_filter(sl, permission_search_term):

    when(sl).input_text(
        locator=locator['add_group_page']['input_permission_field'],
        text=permission_search_term
    ).thenReturn(None)

    dropdown_text = do_get_text_for_available_permissions_dropdown(permission_search_term)
    when(sl).get_text(locator=locator['add_group_page']['available_permissions_dropdown']).thenReturn(dropdown_text)


def do_get_text_for_available_permissions_dropdown(permission_search_term):
    if permission_search_term == 'blog':
        return expected['add_group_page']['postings-blog post-can_add_blog_post'] + ' ' + \
               expected['add_group_page']['postings-blog post-can_add_blog_post'] + ' ' + \
               expected['add_group_page']['postings-blog post-can_add_blog_post']
    elif permission_search_term == 'yielding no permissions':
        return ''
    else:
        raise AssertionError(f'What to yield in get_text for "{permission_search_term}"? Implement it here')


def configure_mock_calls_in_verify_add_group_page(sl):
    # wait until title element is visible on add_group_page
    when(sl).wait_until_element_is_visible(locator=locator['add_group_page']['title']).thenReturn(None)

    # check the validity of the url on the add_group_page
    when(sl).get_location().thenReturn(expected_add_group_page_url)

    _configure_mock_calls_in_verify_texts_on_add_group_page(sl)
    _configure_mock_calls_in_verify_links_on_add_group_page(sl)
    _configure_mock_calls_in_verify_the_buttons_on_add_group_page(sl)


def _configure_mock_calls_in_verify_texts_on_add_group_page(sl):
    when(sl).element_text_should_be(
        locator=locator['add_group_page']['breadcrumbs'],
        expected=expected['add_group_page']['breadcrumbs_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['add_group'],
        expected=expected['add_group_page']['add_group_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['name'],
        expected=expected['add_group_page']['name_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['permissions'],
        expected=expected['add_group_page']['permissions_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['available_permissions_title'],
        expected=expected['add_group_page']['available_permissions_title_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['available_permissions_dropdown'],
        expected=expected['add_group_page']['available_permissions_dropdown_content']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['available_permissions_tooltip'],
        attribute='title',
        expected=expected['add_group_page']['available_permissions_tooltip_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['choose_all_permissions'],
        expected=expected['add_group_page']['choose_all_permissions_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['help_to_select_multiple_permissions'],
        expected=expected['add_group_page']['help_to_select_multiple_permissions_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['chosen_permissions_title'],
        expected=expected['add_group_page']['chosen_permissions_text']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['chosen_permissions_tooltip'],
        attribute='title',
        expected=expected['add_group_page']['chosen_permissions_tooltip_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['chosen_permissions_dropdown'],
        expected=expected['add_group_page']['chosen_permissions_dropdown_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['add_group_page']['remove_all_permissions_option'],
        expected=expected['add_group_page']['remove_all_permissions_text']
    ).thenReturn(None)


def _configure_mock_calls_in_verify_links_on_add_group_page(sl):

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['home_link'],
        attribute='href',
        expected=links['add_group_page']['home_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['authentication_and_authorization_link'],
        attribute='href',
        expected=links['add_group_page']['authentication_and_authorization_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['groups_link'],
        attribute='href',
        expected=links['add_group_page']['groups_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['choose_all_permissions_option'],
        attribute='href',
        expected=links['add_group_page']['choose_all_permissions_link']
    ).thenReturn(None)


def configure_mock_calls_in_verify_remove_all_permission_link(sl, chosen_permissions_dropdown_text):
    when(sl).get_text(
        locator=locator['add_group_page']['chosen_permissions_dropdown']
    ).thenReturn(chosen_permissions_dropdown_text)

    if chosen_permissions_dropdown_text:
        when(sl).element_should_be_enabled(
            locator=locator['add_group_page']['remove_all_permissions_option']
        ).thenReturn(None)

        when(sl).element_attribute_value_should_be(
            locator=locator['add_group_page']['remove_all_permissions_option'],
            attribute='class',
            expected=eav['add_group_page']['remove_all_permissions_active']
        ).thenReturn(None)

    else:
        # there are no permissions added to chosen_permissions_dropdown element
        when(sl).element_should_be_enabled(
            locator=locator['add_group_page']['remove_all_permissions_option']
        ).thenReturn(None)

        when(sl).element_attribute_value_should_be(
            locator=locator['add_group_page']['remove_all_permissions_option'],
            attribute='class',
            expected=eav['add_group_page']['remove_all_permissions_inactive']
        ).thenReturn(None)


def _configure_mock_calls_in_verify_the_buttons_on_add_group_page(sl):
    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['save_and_add_another_button'],
        attribute='value',
        expected=expected['add_group_page']['save_and_add_another_button_text']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['save_and_continue_editing_button'],
        attribute='value',
        expected=expected['add_group_page']['save_and_continue_editing_button_text']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['add_group_page']['save_button'],
        attribute='value',
        expected=expected['add_group_page']['save_button_text']
    ).thenReturn(None)


def configure_mock_calls_in_enter_name_for_new_group(sl, group_name):
    when(sl).input_text(locator=locator['add_group_page']['input_name_field'],
                        text=group_name).thenReturn(None)
