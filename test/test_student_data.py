import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.function_network.func_network import SendData
from lib.file_management.file_management_lib import DirManagement
from lib.file_management.create_apikeyfile import *
from lib.file_management.config_editor import ConfigEditor

class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir)
        DirManagement.create_dir(os.path.join(self.path, 'ta'))
        workdata = {
    "workDraft": {
        "outputDraft": ["studentId", 
            "param1", 
            "param2", 
            "comment", 
            "score", 
            "scoreTimestamp"], 
        "fileDraft": "{studentId}_test.zip"
    },
    "scores": [
        {
            "studentId": "6310545000",
            "param1": "100",
            "param2": "print('hello')",
            "comment": "good",
            "score": "10",
            "scoreTimestamp": "100"
        }]
}    
        ConfigEditor('testWork2', self.path).writeconfig()
        with open(os.path.join(self.path, 'ta', "work.json"), "w") as create:
            json.dump(workdata, create)
        removeapikey()
        save('testKey')
        self.post = SendData(parentdir)
        return super().setUp()

    def test_getworkdraft(self):
        """
        return None
        """
        self.assertFalse(self.post.getworkDraft())
        

    def tearDown(self) -> None:
        removeapikey()
        DirManagement.remove_dir(os.path.join(self.path, 'ta'))
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()