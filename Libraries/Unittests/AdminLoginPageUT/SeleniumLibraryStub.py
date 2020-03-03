from mockito import mock, when
from CommonVariables import get_variables
from Locators import locator
from ExpectedLinks import admin_login_page_url
from ExpectedTexts import expected


def configure_mock_calls_in_go_to_admin_login_page(sl):
    when(sl).go_to(url=admin_login_page_url).thenReturn(None)
    when(sl).wait_until_element_is_enabled(locator=locator['admin_login_page']['login_button']).thenReturn(None)
    _configure_mock_calls_in_verify_texts_on_admin_login_page(sl)


def _configure_mock_calls_in_verify_texts_on_admin_login_page(sl):

    when(sl).element_text_should_be(locator=locator['admin_login_page']['title'],
                                    expected=expected['admin_login_page']['title_text']).thenReturn(None)

    when(sl).element_text_should_be(locator=locator['admin_login_page']['username_title'],
                                    expected=expected['admin_login_page']['username_text']).thenReturn(None)

    when(sl).element_text_should_be(locator=locator['admin_login_page']['password_title'],
                                    expected=expected['admin_login_page']['password_text']).thenReturn(None)

    when(sl).element_attribute_value_should_be(
        locator=locator['admin_login_page']['login_button'],
        attribute='value',
        expected=expected['admin_login_page']['login_button_text']).thenReturn(None)


def configure_mock_calls_in_login(sl):
    """
    This method configures the stub calls in login() instance method in AdminLoginPage class.
    :param sl: the mocked selenium library object, to be used by AdminLoginPage
    :return: None
    """
    when(sl).input_text(locator=locator['admin_login_page']['username_field'],
                        text=get_variables()['CREDENTIALS']['valid_admin']['username']).thenReturn(None)

    when(sl).input_password(locator=locator['admin_login_page']['password_field'],
                            password=get_variables()['CREDENTIALS']['valid_admin']['password']).thenReturn(None)

    when(sl).click_element(locator=locator['admin_login_page']['login_button']).thenReturn(None)
