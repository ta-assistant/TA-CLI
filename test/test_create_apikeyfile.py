import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.create_apikeyfile import *
from lib.file_management.file_management_lib import DirManagement


class TestCreate_apikey(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(os.path.expanduser("~") ,"key")
        DirManagement.create_dir(self.path)
        return super().setUp()

    def test_save(self):
        """
        return None
        """
        self.assertIsNone(save_api_key('K4nPEs7RhhCzcjdlvr3X=='))

    def test_readapikey(self):
        """
        return ...
        """
        save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertIs(type(readapikey()), str)


    def test_writeapikey(self):
        """
        return None
        """
        self.assertIsNone(writeapikey('K4nPEs7RhhCzcjdlvr3X=='))

    def test_existapikey(self):
        """
        return boolean
        """
        self.assertTrue(exsitapikey())

    def test_removeapikey(self):
        """
        return None
        """
        self.assertIsNone(removeapikey())

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()