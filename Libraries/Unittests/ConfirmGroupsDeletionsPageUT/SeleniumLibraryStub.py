from mockito import mock, when
from Locators import locator
from ExpectedLinks import links, expected_groups_page_url, base_link
from ExpectedTexts import expected


def get_mocked_sl(method_under_test):
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception
    if method_under_test == 'verify_confirm_group_deletions_page':
        # In ConfirmGroupsDeletionsPageUT, in do_test_verify_confirm_group_deletions_page(),
        # call configure_mock_calls_in_go_to_admin_main_page()
        pass
    elif method_under_test == 'press_confirm_button':
        _configure_mock_calls_in_press_confirm_button(sl)
    else:
        raise AssertionError(f'method_under_test is unknown: {method_under_test}')   # invalid method_under_test
    return sl


def _configure_mock_calls_in_press_confirm_button(sl):
    when(sl).click_element(
        locator=locator['confirm_groups_deletions_page']['confirm_deletion_button']
    ).thenReturn(None)


def configure_mock_calls_in_go_to_admin_main_page(sl, group_name):
    when(sl).wait_until_element_is_enabled(
        locator=locator['confirm_groups_deletions_page']['are_you_sure_headline']
    ).thenReturn(None)
    # at this stage, the page is assumed to be loaded
    # verify that confirm_groups_deletions_page url is correct
    when(sl).get_location().thenReturn(expected_groups_page_url)

    _configure_mock_calls_in_verify_texts_on_confirm_groups_deletions_page(sl, group_name)
    _configure_mock_calls_in_verify_links_on_confirm_groups_deletions_page(sl, group_name)


def _configure_mock_calls_in_verify_texts_on_confirm_groups_deletions_page(sl, group_name):
    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['breadcrumbs'],
        expected=expected['confirm_groups_deletions_page']['breadcrumbs_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['are_you_sure_headline'],
        expected=expected['confirm_groups_deletions_page']['are_you_sure_headline_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['are_you_sure_question'],
        expected=expected['confirm_groups_deletions_page']['are_you_sure_question_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['summary'],
        expected=expected['confirm_groups_deletions_page']['summary_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['objects'],
        expected=expected['confirm_groups_deletions_page']['objects_text']
    ).thenReturn(None)

    group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
    when(sl).element_text_should_be(
        locator=group_locator,
        expected=group_name
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['confirm_groups_deletions_page']['confirm_deletion_button'],
        attribute='value',
        expected=expected['confirm_groups_deletions_page']['confirm_deletion_button_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'],
        expected=expected['confirm_groups_deletions_page']['cancel_deletion_button_text']
    ).thenReturn(None)


def _configure_mock_calls_in_verify_links_on_confirm_groups_deletions_page(sl, group_name):

    when(sl).element_attribute_value_should_be(
        locator=locator['confirm_groups_deletions_page']['home'],
        attribute='href',
        expected=links['confirm_groups_deletions_page']['home_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['confirm_groups_deletions_page']['authentication_and_authorization'],
        attribute='href',
        expected=links['confirm_groups_deletions_page']['authentication_and_authorization_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['confirm_groups_deletions_page']['groups'],
        attribute='href',
        expected=links['confirm_groups_deletions_page']['groups_link']
    ).thenReturn(None)

    # the group to be deleted shows as an item under locator['confirm_groups_deletions_page']['objects']
    url = f'{base_link}/admin/auth/group/23/change/'
    group_locator = locator['confirm_groups_deletions_page']['generic_group_element'] % group_name
    when(sl).get_element_attribute(
        locator=group_locator, attribute='href'
    ).thenReturn(url)

    # cancel_deletion_button
    when(sl).get_element_attribute(
        locator=locator['confirm_groups_deletions_page']['cancel_deletion_button'], attribute='href'
    ).thenReturn(links['confirm_groups_deletions_page']['cancel_deletion_button_link'])
