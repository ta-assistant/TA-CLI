from src.main.student_data import StudentData
from src.main.pre_work import Work
import unittest
from unittest.mock import patch
import os
import sys
import inspect
import json
import shutil
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)



sys.path.insert(0, parentdir)
class TestStudentData(unittest.TestCase):
    def setUp(self) -> None:
        os.mkdir(os.path.join(currentdir,"ta"))
        self.path = currentdir
        self.draft = {"fileDraft": "{studentId}_test.zip", "outputDraft": ["studentId", "paraasdfasdfm1", "param2", "comment", "score", "scoreTimestamp"]}
        self.create_work()

    def test_run_all_passed(self):
        student = StudentData(path=self.path, filename="123456789_test", draft=self.draft)
        with open(os.path.join(self.path, "ta", "work.json"), "r") as workfile:
            scores = json.load(workfile)["scores"]
            workfile.close
        student.prepare_student_data()
        self.assertEqual(student.pre_data,{'scoreTimestamp': 'N/A', 'studentId': '123456789', 'paraasdfasdfm1': 'N/A', 'param2': 'N/A', 'comment': 'N/A', 'score': 'N/A'})
        with patch('src.main.student_data.StudentData.ask', side_effect=[-99,-99,-99,-99]):
            result = student.ask()
        print(result)

    def create_work(self):
        work = Work()
        work.draft = self.draft
        work.workId = "testWork2"
        work.path = currentdir
        work.property_is_ready()
        work.create()


    def tearDown(self) -> None:
        shutil.rmtree(os.path.join(currentdir,"ta"))
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()
