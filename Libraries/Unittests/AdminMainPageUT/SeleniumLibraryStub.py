from mockito import mock, when
from Credentials import DICT__CREDENTIALS
from Locators import locator
from ExpectedLinks import expected_admin_main_page_url
from ExpectedTexts import expected


def get_mocked_sl(method_under_test):
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception
    if method_under_test is 'go_to_admin_main_page':
        _configure_mock_calls_in_go_to_admin_main_page(sl)
    else:
        raise AssertionError(f'method_under_test is unknown: {method_under_test}')   # invalid method_under_test
    return sl


def _configure_mock_calls_in_go_to_admin_main_page(sl):
    when(sl).go_to(expected_admin_main_page_url).thenReturn(None)
