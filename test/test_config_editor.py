import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.config_editor import *
from lib.file_management.file_management_lib import DirManagement


class TestConfig_editor(unittest.TestCase):
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

        with open(os.path.join(self.path, "work.json"), "w") as create:
            json.dump(workdata, create)
        writeconfig(parentdir, 'testWork2')
        return super().setUp()

    def test_writeconfig(self):
        """
        return None
        """
        self.assertIsNone(writeconfig(parentdir))


    def test_readconfig(self):
        """
        return str
        """
        self.assertIs(type(readconfig(parentdir)), dict)

    def test_ishaveconfig(self):
        """
        return None
        """
        self.assertIsNone(ishaveconfig(parentdir))

    def test_checkdata(self):
        """
        return None
        """
        self.assertIsNone(checkdata(parentdir))

    def tearDown(self) -> None:
        """
        retrun None
        """
        DirManagement.remove_dir(os.path.join(parentdir,"ta"))
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()