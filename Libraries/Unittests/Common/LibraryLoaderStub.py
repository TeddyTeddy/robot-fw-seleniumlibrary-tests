from mockito import mock, when
from LibraryLoader import LibraryLoader
from SeleniumLibraryStub import get_mocked_sl


def configure_mock_library_loader():
    _ll = mock({
        'sl': get_mocked_sl(),
    }, spec=LibraryLoader)
    when(LibraryLoader).get_instance().thenReturn(_ll)

