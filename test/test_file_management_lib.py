
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
filecurrent = os.path.join(parentdir, "function_network")
sys.path.insert(0,filecurrent)

from lib.file_management.file_management_lib import DirManagement

class TestDirManagement(unittest.TestCase):
    def test_create_dir(self):
        """
        parameter: path: str + your dir name
        return bool -> if directory has been create return Ture else False
        """
        dirmanage = DirManagement()
        self.assertTrue(dirmanage.create_dir(currentdir+"test1"))
        self.assertFalse(dirmanage.create_dir(currentdir+"test1"))

    def test_remove_dir(self):
        """
        parameter: path: str + your dir name
        return bool -> if directory has been remove return Ture else False
        """
        dirmanage = DirManagement()
        self.assertTrue(dirmanage.remove_dir(currentdir+"test1"))
        self.assertFalse(dirmanage.remove_dir(currentdir+"test1"))

    



if __name__ == '__main__':
    unittest.main()