from mockito import mock, when
from Locators import locator
from ExpectedLinks import links, expected_groups_page_url, base_link
from ExpectedTexts import expected


def get_mocked_sl(method_under_test):
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception
    if method_under_test == 'verify_groups_page_loaded':
        # in GroupsPageUT, in test_verify_groups_page_loaded(), call
        # configure_mock_calls_in_verify_groups_page_loaded()
        pass
    elif method_under_test == 'verify_group_added':
        # In GroupsPageUT, in do_test_verify_group_added(), call
        # configure_mock_calls_in_verify_group_added()
        pass
    elif method_under_test == 'select_checkbox_for_group':
        # In GroupsPageUT, in do_test_select_checkbox_for_group(), call
        # configure_mock_calls_in_select_checkbox_for_group()
        pass
    elif method_under_test == 'select_delete_selected_groups_dropdown':
        _configure_mock_calls_in_select_delete_selected_groups_dropdown(sl)
    elif method_under_test == 'press_go':
        _configure_mock_calls_in_press_go(sl)
    else:
        raise AssertionError(f'method_under_test is unknown: {method_under_test}')   # invalid method_under_test
    return sl


def _configure_mock_calls_in_press_go(sl):
    when(sl).click_element(locator=locator['groups_page']['go_button']).thenReturn(None)


def _configure_mock_calls_in_select_delete_selected_groups_dropdown(sl):
    when(sl).click_element(locator=locator['groups_page']['delete_selected_groups_option']).thenReturn(None)


def configure_mock_calls_in_select_checkbox_for_group(sl, group_name):
    group_element_checkbox_locator = locator['groups_page']['generic_group_element_checkbox'] % group_name
    when(sl).click_element(locator=group_element_checkbox_locator).thenReturn(None)


def configure_mock_calls_in_verify_group_added(sl, group_name):
    locator_formatter = locator['groups_page']['generic_group_element'] % group_name
    when(sl).element_text_should_be(
        locator=locator_formatter,
        expected=group_name
    ).thenReturn(None)


def configure_mock_calls_in_verify_groups_page_loaded(sl, group_name):
    when(sl).wait_until_element_is_enabled(
        locator=locator['groups_page']['select_group_to_change']
    ).thenReturn(None)
    # groups_page is loaded at this point
    # verify that groups_page url is correct
    when(sl).get_location().thenReturn(expected_groups_page_url)

    _configure_mock_calls_in_verify_texts_on_groups_page(sl, group_name)
    _configure_mock_calls_in_verify_links_on_groups_page(sl, group_name)


def _configure_mock_calls_in_verify_texts_on_groups_page(sl, group_name):
    when(sl).element_text_should_be(
        locator=locator['groups_page']['breadcrumbs'],
        expected=expected['groups_page']['breadcrumbs_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['home_link'],
        expected=expected['groups_page']['home_link_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['authentication_and_authorization_link'],
        expected=expected['groups_page']['authentication_and_authorization_link_text']
    ).thenReturn(None)

    _configure_mock_calls_in_verify_dynamic_text_group_x_added_successfully(sl, group_name)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['select_group_to_change'],
        expected=expected['groups_page']['select_group_to_change_text']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['groups_page']['search_button'],
        attribute='value',
        expected=expected['groups_page']['search_button_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['action'],
        expected=expected['groups_page']['action_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['delete_selected_groups_option'],
        expected=expected['groups_page']['delete_selected_groups_option_text']
    ).thenReturn(None)

    _configure_mock_calls_in_verify_dynamic_text_x_of_y_selected(sl)

    when(sl).element_text_should_be(
        locator=locator['groups_page']['select_all_groups'],
        expected=expected['groups_page']['select_all_groups_text']
    ).thenReturn(None)


def _configure_mock_calls_in_verify_dynamic_text_x_of_y_selected(sl):
    when(sl).get_text(locator=locator['groups_page']['x_of_y_selected']).thenReturn('0 of 5 selected')
    when(sl).get_text(locator=locator['groups_page']['y_groups']).thenReturn('5 groups')


def _configure_mock_calls_in_verify_dynamic_text_group_x_added_successfully(sl, group_name):
    group_x_added_successfully_text = expected['groups_page']['group_x_added_successfully_text'] % group_name

    when(sl).element_text_should_be(
        locator=locator['groups_page']['group_x_added_successfully'],
        expected=group_x_added_successfully_text
    ).thenReturn(None)


def _configure_mock_calls_in_verify_links_on_groups_page(sl, group_name):
    when(sl).element_attribute_value_should_be(
        locator=locator['groups_page']['home_link'],
        attribute='href',
        expected=links['groups_page']['home_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['groups_page']['authentication_and_authorization_link'],
        attribute='href',
        expected=links['groups_page']['authentication_and_authorization_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['groups_page']['add_group'],
        attribute='href',
        expected=links['groups_page']['add_group_link']
    ).thenReturn(None)

    _configure_mock_calls_in_verify_dynamic_link_for_group_name(sl, group_name)


def _configure_mock_calls_in_verify_dynamic_link_for_group_name(sl, group_name):
    url = f'{base_link}/admin/auth/group/23/change/'
    locator_formatter = locator['groups_page']['generic_group_element'] % group_name
    when(sl).get_element_attribute(
        locator=locator_formatter,
        attribute='href').thenReturn(url)
