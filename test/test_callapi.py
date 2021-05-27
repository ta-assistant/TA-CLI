import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.file_management.function_network.func_network import CallApi
from lib.file_management.file_management_lib import FileEditor, DirManagement

class TestCallApi(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        data = "[CONFIG]\nprefix = https://ta-api.sirateek.dev/"
        with open(os.path.join(self.path, "config.txt"), "w") as create:
            create.write(data)
            print("config.txt has been init.")
            create.close()
        self.call = CallApi('K4nPEs7RhhCzcjdlvr3X==', 'testWork2', parentdir)
        return super().setUp()

    def TestCreateWork(self):
        """
        print(str)
        """
        self.assertIs(type(self.call.createworkdraft()), str)

    def TestWritejson(self):
        """
        print(str)
        """
        self.assertIs(type(self.call.writejson()), str)

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()