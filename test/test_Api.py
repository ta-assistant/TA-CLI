import unittest
import os, sys, inspect, json, requests
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.function_network.func_network import Api
from lib.file_management.file_management_lib import DirManagement
from lib.file_management.create_apikeyfile import *

class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        self.data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workId" : 'testWork2',
                "apikeydir" : os.path.join(os.path.expanduser("~"), 'key')}
        with open(os.path.join(self.path, 'config.json'), "w") as wri:
            json.dump(self.data, wri)
        removeapikey()
        save_api_key('testKey')
        self.api = Api(parentdir)
        self.api.res = requests.get(self.api.url, headers=self.api.hparameter)
        return super().setUp()

    def test_api_massage(self):
        """
        return dict
        """
        self.assertIs(type(self.api.api_massage()), dict)

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        removeapikey()
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()