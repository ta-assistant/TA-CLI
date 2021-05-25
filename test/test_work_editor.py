import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from lib.file_management.file_management_lib import WorkEditor, DirManagement


class TestWorkEditor(unittest.TestCase):
    
    def setUp(self) -> None:
        """
        init we
        init draft.json into list of key
        """
        self.we = WorkEditor()
        self.draft = {"workDraft":{
    "fileDraft": "{student_id}_{name}_{ex}.zip",
    "outputDraft": [
      "student_id",
      "name",
      "ex",
      "score1",
      "score2",
      "comment"
    ]
  }}
        DirManagement.create_dir(os.path.join(currentdir,"ta"))
        return super().setUp()

    # def test_init_work(self):
    #     """
    #     create work.json if it can created return ture else false
    #     and delete it if it can be deleted retrun true else flase
    #     """ 
    #     self.assertTrue(self.we.create_file_work(currentdir))
    #     self.assertFalse(self.we.create_file_work(currentdir))

    def test_write_work(self):
        """
        create work.json if it can created return ture else false
        call write_work() if it can write return true else false
        and delete it if it can be deleted retrun true else flase
        """
        self.assertTrue(self.we.create_file_work(currentdir))
        self.assertFalse(self.we.create_file_work(currentdir))
        self.we.add_workid(currentdir,123456)
        self.assertEqual(self.we.read_work(currentdir),{'workId': '123456', 'workDraft': "N/A", 'scores': []})
        self.we.add_draft(currentdir,self.draft)
        self.assertEqual(self.we.read_work(currentdir),{'workId': '123456', 'workDraft': {'workDraft': {'fileDraft': '{student_id}_{name}_{ex}.zip', 'outputDraft': ['student_id', 
'name', 'ex', 'score1', 'score2', 'comment']}}, 'scores': []})
        stu_data = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'}
        self.assertIsNone(self.we.write_work(currentdir,stu_data))
        self.assertEqual(self.we.read_work(currentdir),{
  "workId": "123456",
  "workDraft": {
    "workDraft": {
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
  },
  "scores": [
    {
      "student_id": "6310546066",
      "name": "vitvara",
      "ex": "ex1",
      "score1": "12",
      "score2": "13",
      "comment": "nice work"
    }
  ]
})

    def tearDown(self) -> None:
        DirManagement.remove_dir(os.path.join(currentdir,"ta"))
        return super().tearDown()
if __name__ == "__main__":
    unittest.main()