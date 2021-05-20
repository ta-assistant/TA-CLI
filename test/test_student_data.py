import unittest
from unittest.mock import patch
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from src.main.student_data import StudentData


class TestStuData(unittest.TestCase):
    @patch("make.data_input",return_value='1')
    def test_add_student_data(self):
        stu1 = StudentData(currentdir,"6310546066_vitvara_ex1")
        self.assertEqual(stu1.ask(),{'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'})

if __name__ == "__main__":
    unittest.main()