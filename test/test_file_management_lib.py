
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from lib.file_management import file_management_lib


class TestFileEditor(unittest.TestCase):
    def test_create_file(self):
        """
        parameter: path: str, filename: str
        return None

        """
        file_editor = file_management_lib.FileEditor()
        self.assertIsNone(file_editor.create_file(currentdir,r"\test.txt"))

    def test_read_file(self):
        """
        pass
        """
        file_editor = file_management_lib.FileEditor()
        self.assertIsNone(file_editor.read_file(currentdir,r"test.txt"))

    def test_delete_file(self):
        """
        parameter: path: str, filename: str
        return bool -> if file has been delete return True else: False
        """
        file_editor = file_management_lib.FileEditor()
        self.assertTrue(file_editor.delete_file(currentdir,r"\test.txt"))
        self.assertFalse(file_editor.delete_file(currentdir,r"\test.txt"))


class TestDirManagement(unittest.TestCase):
    def test_create_dir(self):
        """
        parameter: path: str + your dir name
        return bool -> if directory has been create return Ture else False
        """
        dirmanage = file_management_lib.DirManagement()
        self.assertTrue(dirmanage.create_dir(currentdir+r"\test1"))
        self.assertFalse(dirmanage.create_dir(currentdir+r"\test1"))

    def test_remove_dir(self):
        """
        parameter: path: str + your dir name
        return bool -> if directory has been remove return Ture else False
        """
        dirmanage = file_management_lib.DirManagement()
        self.assertTrue(dirmanage.remove_dir(currentdir+r"\test1"))
        self.assertFalse(dirmanage.remove_dir(currentdir+r"\test1"))

    



if __name__ == '__main__':
    unittest.main()