from mockito import mock, when
from Credentials import DICT__CREDENTIALS
from Locators import locator


def get_mocked_sl():
    # _sl stands for selenium library
    _sl = mock(strict=True)     # every un-configured, unexpected call on _sl will raise an exception
    _configure_mock_calls_in_login(_sl)
    return _sl


def _configure_mock_calls_in_login(_sl):
    """
    This method configures the stub calls in login() instance method in AdminLoginPage class.
    :param _sl: the mocked selenium library object, to be used by AdminLoginPage
    :return: None
    """
    when(_sl).input_text(locator=locator['admin_login_page']['username_field'],
                         text=DICT__CREDENTIALS['valid_admin']['username']).thenReturn(None)

    when(_sl).input_password(locator=locator['admin_login_page']['password_field'],
                             password=DICT__CREDENTIALS['valid_admin']['password']).thenReturn(None)

    when(_sl).click_element(locator=locator['admin_login_page']['login_button']).thenReturn(None)
