from mockito import mock, when
from LibraryLoader import LibraryLoader
from SeleniumLibraryStub import get_mocked_sl


def configure_mock_library_loader(method_under_test):
    _ll = mock({
        'sl': get_mocked_sl(method_under_test),
    }, spec=LibraryLoader)
    when(LibraryLoader).get_instance().thenReturn(_ll)

