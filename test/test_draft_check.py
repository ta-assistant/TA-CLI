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
        """
        create env in test dir:
        - ~/ta
        - ~/ta/draft.json
        """
        self.ta_dir = os.path.join(currentdir,"ta")
        DirManagement().create_dir(self.ta_dir)
        FileEditor().create_file(self.ta_dir,"draft.json")
        return super().setUp()

    def test_check_draft(self):
        """call function check_draft need to be return True
        """
        self.assertTrue(check_draft(currentdir))
        
    def tearDown(self) -> None:
        """
        remove ~/ta when the test is finish
        """
        DirManagement().remove_dir(currentdir+r"\ta")
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()