import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from src.main.draft_check import check_draft
from lib.file_management.file_management_lib import DirManagement, FileEditor

class TestDraftCheck(unittest.TestCase):
    def setUp(self) -> None:
        DirManagement().create_dir(currentdir+r"\ta")
        FileEditor().create_file(currentdir+r"\ta",r"\draft.json")
        return super().setUp()

    def test_check_draft(self):
        self.assertTrue(check_draft(currentdir))
        
    def tearDown(self) -> None:
        DirManagement().remove_dir(currentdir+r"\ta")
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()