import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.function_network.func_network import CallApi
from lib.file_management.file_management_lib import DirManagement

class TestCallApi(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workID" : 'testWork2'}
        with open(os.path.join(self.path, 'ta', 'config.json'), "w") as wri:
            json.dump(data, wri)
        self.call = CallApi('K4nPEs7RhhCzcjdlvr3X==', parentdir)
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