import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.function_network.func_network import SendData
from lib.file_management.file_management_lib import DirManagement
from lib.file_management.createapikeyfile import SaveApiKey

class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(parentdir,"ta")
        DirManagement.create_dir(self.path)
        workdata = {
    "workDraft": {
        "outputDraft": [
            "ID",
            "param1",
            "param2",
            "comment"
        ],
        "fileDraft": "{ID}_test.py"
    },
    "scores": [
        {
            "ID": "6310545000",
            "param1": "100",
            "param2": "print('hello')",
            "comment": "good"
        }]
}
        data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workId" : 'testWork2'}
        with open(os.path.join(self.path, 'config.json'), "w") as wri:
            json.dump(data, wri)
        with open(os.path.join(self.path, "work.json"), "w") as create:
            json.dump(workdata, create)
        SaveApiKey().removeapikey()
        SaveApiKey().save('K4nPEs7RhhCzcjdlvr3X==')
        self.post = SendData(parentdir)
        return super().setUp()

    def testgetworkdraft(self):
        """
        return None
        """
        self.assertIsNone(self.post.getworkDraft())
        


    def tearDown(self) -> None:
        SaveApiKey().removeapikey()
        DirManagement.remove_dir(self.path)
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()