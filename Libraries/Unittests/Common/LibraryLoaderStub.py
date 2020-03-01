from mockito import mock, when
from LibraryLoader import LibraryLoader


def configure_mock_library_loader():
    # sl stands for selenium library
    sl = mock(strict=True)     # every un-configured, unexpected call on sl will raise an exception

    # You can also create an empty Mock which is specced against a given spec: spec=LibraryLoader.
    # These mock are by default strict, thus they raise if you want to stub a method, the spec does not implement.
    # Mockito will also match the function signature.
    ll = mock({
        'sl': sl,
    }, spec=LibraryLoader)
    when(LibraryLoader).get_instance().thenReturn(ll)

