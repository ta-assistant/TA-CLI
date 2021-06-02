import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.createapikeyfile import SaveApiKey
from lib.file_management.file_management_lib import DirManagement


class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        self.key = SaveApiKey(parentdir)
        self.key.save('K4nPEs7RhhCzcjdlvr3X==')

    def testsave(self):
        """
        return None
        """
        self.assertIsNone(self.key.save('K4nPEs7RhhCzcjdlvr3X=='))

    def testreadapikey(self):
        """
        return ...
        """
        self.assertIs(type(self.key.readapikey()), dict)

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()