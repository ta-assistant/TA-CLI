import unittest
from unittest.mock import patch
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0,parentdir)

from src.main.student_data import StudentData


class TestStuData(unittest.TestCase):
    def setUp(self) -> None:
        self.draft = {
      "fileDraft": "{student_id}_{name}_{ex}.zip",
      "outputDraft": [
        "student_id",
        "name",
        "ex",
        "score1",
        "score2",
        "comment"
      ]
    }


        return super().setUp()

    @patch("src.main.student_data.inask",return_value='1')
    def test_add_student_data(self,input):
        """
        test that when we have perfect env then it will produce a perfect data that we need
        """
    
        stu1 = StudentData(currentdir,"6310546066_vitvara_ex1",self.draft)
        stu1.prepare_student_data()
        self.assertEqual(stu1.pre_data,{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': 'N/A', 'score2': 'N/A', 'comment': 'N/A'})
        self.assertEqual(stu1.ask(),{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '1', 'score2': '1', 'comment': '1'})

    @patch("src.main.student_data.inask",return_value='-99')
    def test_skip(self,input):
        stu1 = StudentData(currentdir,"6310546066_vitvara_ex1",self.draft)
        stu1.prepare_student_data()
        self.assertEqual(stu1.pre_data,{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': 'N/A', 'score2': 'N/A', 'comment': 'N/A'})
        self.assertEqual(stu1.ask(),{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': 'N/A', 'score2': 'N/A', 'comment': 'N/A'})
        
if __name__ == "__main__":
    unittest.main()