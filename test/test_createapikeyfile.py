import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.createapikeyfile import SaveApiKey
from lib.file_management.file_management_lib import DirManagement


class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(os.path.expanduser("~") ,"key")
        DirManagement.create_dir(self.path)
        self.key = SaveApiKey()
        return super().setUp()

    def test_save(self):
        """
        return None
        """
        self.assertIsNone(self.key.save('K4nPEs7RhhCzcjdlvr3X=='))

    def test_readapikey(self):
        """
        return ...
        """
        self.key.save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertIs(type(self.key.readapikey()), str)


    def test_writeapikey(self):
        """
        return None
        """
        self.assertIsNone(self.key.writeapikey('K4nPEs7RhhCzcjdlvr3X=='))

    def test_existapikey(self):
        """
        return boolean
        """
        self.assertTrue(self.key.exsitapikey())

    def test_removeapikey(self):
        """
        return None
        """
        self.assertIsNone(self.key.removeapikey())

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()