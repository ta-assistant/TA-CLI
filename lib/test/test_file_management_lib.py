
import unittest
from unittest.mock import MagicMock
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from file_management import file_management_lib


def format_test(testname):
    print("\n=======================")
    print("Test "+testname+"\n")


class TestFileEditor(unittest.TestCase):

    def test_create_file(self):
        format_test("create_file()")
        file_editor = file_management_lib.FileEditor()
        self.assertIsNone(file_editor.create_file(currentdir,r"\test.txt"))
        print("done")

    def test_read_file(self):
        format_test("read_file()")
        file_editor = file_management_lib.FileEditor()
        self.assertIsNone(file_editor.read_file(currentdir,r"test.txt"))
        print("done")

    def test_delete_file(self):
        format_test("delete_file()")
        file_editor = file_management_lib.FileEditor()
        self.assertTrue(file_editor.delete_file(currentdir,r"\test.txt"))
        self.assertFalse(file_editor.delete_file(currentdir,r"\test.txt"))
        print("done")


class TestDirManagement(unittest.TestCase):
    def test_create_dir(self):
        format_test("create_dir()")
        dirmanage = file_management_lib.DirManagement()
        self.assertTrue(dirmanage.create_dir(currentdir+r"\test1"))
        self.assertFalse(dirmanage.create_dir(currentdir+r"\test1"))
        print("done")

    def test_remove_dir(self):
        format_test("remove_dir()")
        dirmanage = file_management_lib.DirManagement()
        self.assertTrue(dirmanage.remove_dir(currentdir+r"\test1"))
        self.assertFalse(dirmanage.remove_dir(currentdir+r"\test1"))
        print("done")
    



if __name__ == '__main__':
    unittest.main()