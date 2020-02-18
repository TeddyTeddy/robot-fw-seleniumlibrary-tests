from mockito import mock, when
from LibraryLoader import LibraryLoader
from SeleniumLibraryStub import get_mocked_sl


def mock_library_loader_and_selenium_library():
    _ll = mock({
        'sl': get_mocked_sl(),
    }, spec=LibraryLoader)
    when(LibraryLoader).get_instance().thenReturn(_ll)

