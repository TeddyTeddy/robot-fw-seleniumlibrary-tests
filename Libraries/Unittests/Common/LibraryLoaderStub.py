from mockito import mock, when
from LibraryLoader import LibraryLoader


def configure_mock_library_loader():
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception

    ll = mock({
        'sl': sl,
    }, spec=LibraryLoader)
    when(LibraryLoader).get_instance().thenReturn(ll)

