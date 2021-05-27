import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.function_network.func_network import Writeconfig
from lib.file_management.file_management_lib import DirManagement


class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        self.wr = Writeconfig('testWork2', parentdir)
        return super().setUp()

    def testwriteworkid_path(self):
        """
        return None
        """
        self.assertIsNone(self.wr.writeworkid_path())

    def tearDown(self) -> None:
        DirManagement.remove_dir(os.path.join(parentdir,"ta"))
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()