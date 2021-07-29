import unittest
from unittest.mock import patch
import os, inspect, shutil
import json
from src.main.pre_work import Work

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class TestPreWork(unittest.TestCase):
    def setUp(self):
        self.work = Work()
        return super().setUp()

    def test_assigne_work(self):
        self.work.workId = 123456 
        self.assertTrue(self.work.workId_state)

    def test_assign_draft(self):
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
        self.assertTrue(self.work.draft_state)
    
    def test_assign_path(self):
        self.work.path = currentdir
        self.assertTrue(self.work.path_state)
    
    def test_assign_draft_error(self):
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'scoreTimestamp']}
        self.assertFalse(self.work.draft_state)
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['param1', 'param2', 'comment','score', 'scoreTimestamp']}
        self.assertFalse(self.work.draft_state)
        self.work.draft = {"outputDraft": ['studentId', 'param1', 'param2', 'comment','score', 'scoreTimestamp']}
        self.assertFalse(self.work.draft_state)
        self.work.draft = {"fileDraft": "{studentId}_test.zip"}
        self.assertFalse(self.work.draft_state)
        
    def test_assign_path_error(self):
        self.work.path = "123456"
        self.assertFalse(self.work.path_state)
    
    def test_check_property_is_ready(self):
        self.work.workId = 123456 
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
        self.work.path = currentdir
        self.assertTrue(self.work.property_is_ready())

    def test_check_property_is_not_ready(self):
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'scoreTimestamp']}
        self.work.path = "123456"
        self.work.workId = 123456 
        self.assertFalse(self.work.property_is_ready())
        self.work.draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
        self.assertFalse(self.work.property_is_ready())
        self.work.path = currentdir
        self.assertTrue(self.work.property_is_ready())

    def test_create(self):
        os.mkdir(os.path.join(currentdir,"ta"))
        self.work.workId = 123456 
        self.work.draft = {'fileDraft': '{studentId}_test.zip','outputDraft': ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
        self.work.path = currentdir
        self.assertTrue(self.work.create())
        work_file = open(os.path.join(currentdir,"ta","work.json"), "r")
        work_data = work_file.read()
        work_file.close()
        self.maxDiff = None
        self.assertEqual(work_data,json.dumps({"workId": "123456", "workDraft": {"fileDraft": "{studentId}_test.zip", "outputDraft": ["studentId", "param1", "param2", "comment", "score", "scoreTimestamp"]}, "scores": []}))

    def test_write_work(self):
        param_list = [{
                                "scoreTimestamp": 1627484331095,
                                "studentId": "6310541066",
                                "param1": "1",
                                "param2": "2",
                                "comment": "3",
                                "score": 1.0
                            },{
      "scoreTimestamp": 1627484336745,
      "studentId": "6310542066",
      "param1": "2",
      "param2": "3",
      "comment": "2",
      "score": 1.0
    },
    {
      "scoreTimestamp": 1627484338382,
      "studentId": "6310545066",
      "param1": "2",
      "param2": "3",
      "comment": "1",
      "score": 2.0
    }]  
        for student_score in param_list:
            os.mkdir(os.path.join(currentdir,"ta"))
            self.work.workId = 123456 
            self.work.draft = {'fileDraft': '{studentId}_test.zip','outputDraft': ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
            self.work.path = currentdir
            self.work.create()
            self.work.write_work(student_score)
            self.work.write_work(student_score)
            work_file = open(os.path.join(currentdir,"ta","work.json"), "r")
            work_str = work_file.read()
            work_data = json.loads(work_str)
            work_file.close()
            self.assertEqual(work_data["scores"],[student_score,student_score])
            self.tearDown()

        

    def tearDown(self) -> None:
        if os.path.exists(os.path.join(currentdir,"ta")):
            shutil.rmtree(os.path.join(currentdir,"ta"))
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()