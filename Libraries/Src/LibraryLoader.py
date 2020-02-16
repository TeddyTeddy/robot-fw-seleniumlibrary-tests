from robot.libraries.BuiltIn import BuiltIn


class LibraryLoader:
    """
    https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """
    __instance = None

    def __init__(self):
        if LibraryLoader.__instance is not None:
            raise Exception('LibraryLoader class is a singleton. Use get_instance method instead')
        LibraryLoader.__instance = self
        self._sl = None  # lazy initialization

    @staticmethod
    def get_instance():
        if LibraryLoader.__instance is None:
            LibraryLoader()
        return LibraryLoader.__instance

    @property
    def sl(self):
        if self._sl is None:
            self.sl = BuiltIn().get_library_instance('SeleniumLibrary')  # TODO: the caller receives an exception if any
            self._sl.set_selenium_timeout('20 seconds')         # for events and actions
            self._sl.set_selenium_implicit_wait('20 seconds')   # Heroku page starts up slowly
        return self._sl

    @sl.setter
    def sl(self, sl):
        self._sl = sl



