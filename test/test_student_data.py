import unittest
from unittest.mock import patch
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
maindir = os.path.join(parentdir,"src","main")
sys.path.insert(0,maindir)

import student_data


class TestStuData(unittest.TestCase):

    @patch("student_data.inask",return_value='1')
    def test_add_student_data(self,input):
        stu1 = student_data.StudentData(currentdir,"6310546066_vitvara_ex1")
        stu1.draft_zip = "{student_id}_{name}_{ex}.zip"
        stu1.draft_work = [
                        "student_id",
                        "name",
                        "ex",
                        "score1",
                        "score2",
                        "comment"
                        ]
        stu1.prepare_data()
        self.assertEqual(stu1.pre_data,{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1'})
        stu1.add_pre_student_data(stu1.setup_empty_data())
        self.assertEqual(stu1.pre_data,{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': 'N/A', 'score2': 'N/A', 'comment': 'N/A'})
        self.assertEqual(stu1.ask(),{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '1', 'score2': '1', 'comment': '1'})
    def test_not_have_draft(self):
        stu1 = student_data.StudentData(currentdir,"6310546066_vitvara_ex1")
        self.assertIsNone(stu1.pre_data)
        self.assertIsNone(stu1.draft_zip)
        self.assertIsNone(stu1.draft_work)
if __name__ == "__main__":
    unittest.main()