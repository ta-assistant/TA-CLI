import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from lib.file_management.file_management_lib import WorkEditor


class TestWorkEditor(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        init je
        init draft.json into list of key
        """
        self.je = WorkEditor(currentdir)
        self.je.draft = [
                            "student_id",
                            "name",
                            "ex",
                            "score1",
                            "score2",
                            "comment"
                            ]

        return super().setUp()

    def test_init_work(self):
        """
        create work.json if it can created return ture else false
        and delete it if it can be deleted retrun true else flase
        """ 
        self.assertTrue(self.je.create_file_work())
        self.assertFalse(self.je.create_file_work())
        self.assertTrue(self.je.delete_file(currentdir,"work.json"))
        self.assertFalse(self.je.delete_file(currentdir,"work.json"))

    def test_write_work(self):
        """
        create work.json if it can created return ture else false
        call write_work() if it can write return true else false
        and delete it if it can be deleted retrun true else flase
        """
        self.assertTrue(self.je.create_file_work())
        self.assertFalse(self.je.create_file_work())
        stu_data = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'}
        self.assertIsNone(self.je.write_work(stu_data))
        stu_data = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'scdfe2': '13', 'comment': 'nice work'}
        self.assertIsNone(self.je.write_work(stu_data))
        self.assertTrue(self.je.delete_file(currentdir,"work.json"))
        self.assertFalse(self.je.delete_file(currentdir,"work.json"))

    def test_remove_work(self):
        """
        create work.json if it can created return ture else false
        and delete it if it can be deleted retrun true else flase
        """
        self.assertTrue(self.je.create_file_work())
        self.assertFalse(self.je.create_file_work())
        self.assertTrue(self.je.delete_file(currentdir,"work.json"))
        self.assertFalse(self.je.delete_file(currentdir,"work.json"))

if __name__ == "__main__":
    unittest.main()