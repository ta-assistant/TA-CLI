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

    def testsave(self):
        """
        return None
        """
        self.assertIsNone(self.key.save('K4nPEs7RhhCzcjdlvr3X=='))

    def testreadapikey(self):
        """
        return ...
        """
        self.key.save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertIs(type(self.key.readapikey()), str)

    def testriteapikey(self):
        """
        return None
        """
        self.assertIsNone(self.key.writeapikey('K4nPEs7RhhCzcjdlvr3X=='))

    def testexistapikey(self):
        """
        return boolean
        """
        self.assertFalse(self.key.exsitapikey())
        self.key.save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertTrue(self.key.exsitapikey())

    def testremoveapikey(self):
        """
        return None
        """
        self.assertIsNone(self.key.removeapikey())

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()