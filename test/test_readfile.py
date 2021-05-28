import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.function_network.func_network import ReadFile
from lib.file_management.file_management_lib import DirManagement

class TestReadFile(unittest.TestCase):
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

        with open(os.path.join(parentdir, 'ta', 'config.txt'), "w") as wri:
            wri.write("[CONFIG]\nprefix = https://ta-api.sirateek.dev/")
            wri.write(f'\nworkID = testWork2')
            print("config.txt has been create")
            wri.close()
        with open(os.path.join(self.path, "work.json"), "w") as create:
            json.dump(workdata, create)
        self.fread = ReadFile()
        return super().setUp()

    def testfileread(self):
        """
        return str
        """
        self.assertIs(type(self.fread.fileread(parentdir, 'config.txt')), tuple)

    def tearDown(self) -> None:
        DirManagement.remove_dir(os.path.join(parentdir,"ta"))
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()