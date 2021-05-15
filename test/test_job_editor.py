import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir+r"\lib\file_management")

import job_editor as je


class TestJobEditor(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        init job_editor
        init draft.json into list of key
        """
        self.job_editor = je.JobEditor(currentdir)
        self.job_editor.draft = [
                            "student_id",
                            "name",
                            "ex",
                            "score1",
                            "score2",
                            "comment"
                            ]

        return super().setUp()

    def test_init_job(self):
        """
        create job.json if it can created return ture else false
        and delete it if it can be deleted retrun true else flase
        """ 
        self.assertTrue(self.job_editor.create_file_job())
        self.assertFalse(self.job_editor.create_file_job())
        self.assertTrue(self.job_editor.delete_file(currentdir,"\job.json"))
        self.assertFalse(self.job_editor.delete_file(currentdir,"\job.json"))

    def test_write_job(self):
        """
        create job.json if it can created return ture else false
        call write_job() if it can write return true else false
        and delete it if it can be deleted retrun true else flase
        """
        self.assertTrue(self.job_editor.create_file_job())
        self.assertFalse(self.job_editor.create_file_job())
        stu_data = ["6310546066", "vitvara", "ex1", "12", "13", "nice job"]
        self.assertTrue(self.job_editor.write_job(stu_data))
        stu_data = ["6310546066", "vitvara", "ex1", "12", "13"]
        self.assertFalse(self.job_editor.write_job(stu_data))
        self.assertTrue(self.job_editor.delete_file(currentdir,"\job.json"))
        self.assertFalse(self.job_editor.delete_file(currentdir,"\job.json"))

    def test_remove_job(self):
        """
        create job.json if it can created return ture else false
        and delete it if it can be deleted retrun true else flase
        """
        self.assertTrue(self.job_editor.create_file_job())
        self.assertFalse(self.job_editor.create_file_job())
        self.assertTrue(self.job_editor.delete_file(currentdir,"\job.json"))
        self.assertFalse(self.job_editor.delete_file(currentdir,"\job.json"))

if __name__ == "__main__":
    unittest.main()