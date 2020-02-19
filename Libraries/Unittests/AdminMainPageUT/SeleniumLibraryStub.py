from mockito import mock, when
from Credentials import DICT__CREDENTIALS
from Locators import locator, number_of_add_buttons, number_of_change_buttons
from ExpectedLinks import expected_admin_main_page_url, links
from ExpectedTexts import expected


def get_mocked_sl(method_under_test):
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception
    if method_under_test is 'go_to_admin_main_page':
        _configure_mock_calls_in_go_to_admin_main_page(sl)
    elif method_under_test is 'verify_admin_main_page':
        _configure_mock_calls_in_verify_admin_main_page(sl)
    elif method_under_test is 'click_on_add_group_button':
        _configure_mock_calls_in_click_on_add_group_button(sl)
    else:
        raise AssertionError(f'method_under_test is unknown: {method_under_test}')   # invalid method_under_test
    return sl


def _configure_mock_calls_in_go_to_admin_main_page(sl):
    when(sl).go_to(expected_admin_main_page_url).thenReturn(None)


def _configure_mock_calls_in_verify_admin_main_page(sl):
    when(sl).wait_until_element_is_enabled(locator=locator['admin_main_page']['logout']).thenReturn(None)
    when(sl).get_location().thenReturn(expected_admin_main_page_url)
    _configure_mock_calls_in_verify_texts_on_admin_main_page(sl, username=DICT__CREDENTIALS['valid_admin']['username'])
    _configure_mock_calls_in_verify_links_on_admin_main_page(sl)


def _configure_mock_calls_in_verify_texts_on_admin_main_page(sl, username):

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['main_title'],
        expected=expected['admin_main_page']['main_title_text']
    ).thenReturn(None)

    # user navigation bar on the upper right of the page
    dynamic_user_tab_text = expected['admin_main_page']['dynamic_user_tab_text'] % username.upper()
    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['welcome_user_x'],
        expected=dynamic_user_tab_text
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['view_site'],
        expected=expected['admin_main_page']['view_site_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['change_password'],
        expected=expected['admin_main_page']['change_password_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['logout'],
        expected=expected['admin_main_page']['logout_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['site_administration'],
        expected=expected['admin_main_page']['site_administration_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['authentication_and_authorization'],
        expected=expected['admin_main_page']['authentication_and_authorization_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['groups'],
        expected=expected['admin_main_page']['groups_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['users'],
        expected=expected['admin_main_page']['users_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['postings'],
        expected=expected['admin_main_page']['postings_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['blog_posts'],
        expected=expected['admin_main_page']['blog_posts_text']
    ).thenReturn(None)

    # the number of 'Add' buttons must be number_of_add_buttons
    when(sl).page_should_contain_element(
        locator=locator['admin_main_page']['add_button'],
        limit=number_of_add_buttons
    ).thenReturn(None)

    # the number of 'Change' buttons must be number_of_change_buttons
    when(sl).page_should_contain_element(
        locator=locator['admin_main_page']['change_button'],
        limit=number_of_change_buttons
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['recent_actions'],
        expected=expected['admin_main_page']['recent_actions_text']
    ).thenReturn(None)

    when(sl).element_text_should_be(
        locator=locator['admin_main_page']['my_actions'],
        expected=expected['admin_main_page']['my_actions_text']
    ).thenReturn(None)


def _configure_mock_calls_in_verify_links_on_admin_main_page(sl):

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['main_title'],
        attribute='href',
        expected=links['admin_main_page']['main_title_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['view_site'],
        attribute='href',
        expected=links['admin_main_page']['view_site_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['change_password'],
        attribute='href',
        expected=links['admin_main_page']['change_password_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['logout'],
        attribute='href',
        expected=links['admin_main_page']['logout_link']
    ).thenReturn(None)

    # authentication and authorization section
    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['authentication_and_authorization'],
        attribute='href',
        expected=links['admin_main_page']['authentication_and_authorization_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['groups'],
        attribute='href',
        expected=links['admin_main_page']['groups_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['users'],
        attribute='href',
        expected=links['admin_main_page']['users_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['add_group'],
        attribute='href',
        expected=links['admin_main_page']['add_group_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['change_group'],
        attribute='href',
        expected=links['admin_main_page']['change_group_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['add_user'],
        attribute='href',
        expected=links['admin_main_page']['add_user_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['change_user'],
        attribute='href',
        expected=links['admin_main_page']['change_user_link']
    ).thenReturn(None)

    # postings section
    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['postings'],
        attribute='href',
        expected=links['admin_main_page']['postings_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['blog_posts'],
        attribute='href',
        expected=links['admin_main_page']['blog_posts_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['add_blog_post'],
        attribute='href',
        expected=links['admin_main_page']['add_blog_post_link']
    ).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_main_page']['change_blog_post'],
        attribute='href',
        expected=links['admin_main_page']['change_blog_post_link']
    ).thenReturn(None)


def _configure_mock_calls_in_click_on_add_group_button(sl):
    when(sl).click_link(locator=locator['admin_main_page']['add_group']).thenReturn(None)