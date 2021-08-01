import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.create_apikeyfile import *
from lib.function_network.func_network import CallApi
from lib.file_management.file_management_lib import DirManagement
from lib.file_management.config_editor import *

class TestCallApi(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        self.data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workId" : 'testWork2',
                "apikeydir" : os.path.join(os.path.expanduser("~"), 'key')}
        with open(os.path.join(self.path, 'config.json'), "w") as wri:
            json.dump(self.data, wri)
        removeapikey()
        save('testKey')
        self.call = CallApi(parentdir)
        return super().setUp()

    def Test_apimassage(self):
        """
        return dict
        """
        self.assertIs(type(self.call.api_massage()), dict)

    def Test_fetch(self):
        """
        if success will return dict
        if fail will return boolean
        """
        self.assertIs(self.call.fetch(), dict)
        save('wrongkey')
        self.call = CallApi(parentdir)
        self.assertFalse(self.call.fetch())

    def Test_CreateWork(self):
        """
        print(str)
        """
        self.assertTrue(self.call.createworkdraft())
        save('wrongkey')
        self.call = CallApi(parentdir)
        self.assertFalse(self.call.createworkdraft())


    def test_Writejson(self):
        """
        return None
        """
        self.assertIsNone(self.call.writejson(self.data))
        

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path)
        removeapikey()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()