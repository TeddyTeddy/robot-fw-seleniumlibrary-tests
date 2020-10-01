from robot.libraries.BuiltIn import BuiltIn


class LibraryLoader:
    """
    https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """
    __instance = None

    def __init__(self):
        if self.__class__.__instance is not None:
            raise Exception(f'{self.__class__} is a singleton. Use get_instance() instead')
        self.__class__.__instance = self
        self._sl = None  # lazy initialization

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    @property
    def sl(self):
        if self._sl is None:
            self.sl = BuiltIn().get_library_instance('SeleniumLibrary')  # TODO: the caller receives an exception if any
            self._sl.set_selenium_timeout('20 seconds')         # Wait Until ... keywords
            self._sl.set_selenium_implicit_wait('20 seconds')   # For WebDriver's element queries in DOM
        return self._sl

    @sl.setter
    def sl(self, sl):
        self._sl = sl



