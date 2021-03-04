import os
from unittest import TestCase


# Disable to ignore unimplemented code
fail_not_implemented = False


class CustomTestObject(TestCase):


    has_set_fail_not_implemented = False


    def __init__(self):
        super().__init__()
        self.__set_fail_not_implemented()


    # --------------------------------------------------------------------------
    # Custom assertions
    # --------------------------------------------------------------------------


    def failNotImplemented(self):
        """
        Fail if the function or test is not implemented.
        """
        self.assertFalse(fail_not_implemented, "Not implemented.")


    # --------------------------------------------------------------------------
    # Helpers
    # --------------------------------------------------------------------------


    def __set_fail_not_implemented(self):
        """
        Set fail_not_implemented boolean from environment variable once per run.
        """
        if not CustomTestObject.has_set_fail_not_implemented:
            fail_not_implemented__str = os.getenv("FAIL_NOT_IMPLEMENTED")
            if not (fail_not_implemented__str is None) and not (fail_not_implemented__str == ""):
                fail_not_implemented = bool(fail_not_implemented__str)
        CustomTestObject.has_set_fail_not_implemented = True
