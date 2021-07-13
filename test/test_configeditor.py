import unittest
import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from lib.file_management.configeditor import ConfigEditor
from lib.file_management.file_management_lib import DirManagement


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

        with open(os.path.join(self.path, "work.json"), "w") as create:
            json.dump(workdata, create)
        self.con = ConfigEditor('testWork2', parentdir)
        self.con.writeconfig()
        return super().setUp()

    def test_writeconfig(self):
        """
        return None
        """
        self.assertIsNone(self.con.writeconfig())


    def test_readconfig(self):
        """
        return str
        """
        self.assertIs(type(self.con.readconfig()), dict)

    def test_ishaveconfig(self):
        """
        return None
        """
        self.assertIsNone(self.con.ishaveconfig())

    def test_checkdata(self):
        """
        return None
        """
        self.assertIsNone(self.con.checkdata())

    def tearDown(self) -> None:
        """
        retrun None
        """
        DirManagement.remove_dir(os.path.join(parentdir,"ta"))
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()