import unittest
import os,sys,inspect, shutil
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from src.main.pre_work import Work

class TestWorkEditor(unittest.TestCase):
    
    def setUp(self) -> None:
        self.draft = {"fileDraft": "{studentId}_test.zip", "outputDraft": ["studentId", "paraasdfasdfm1", "param2", "comment", "score", "scoreTimestamp"]}
        self.config = {"workId":"testWork2"}
        os.mkdir(os.path.join(currentdir,"ta"))

    def test_work_run_all_passed(self):
        work = Work()
        work.draft = self.draft
        work.workId = "testWork2"
        work.path = currentdir
        self.assertTrue(work.property_is_ready())
        work_path = os.path.join(currentdir, "ta", "work.json")
        self.assertTrue(work.create())
    
    def test_run_again(self):
        self.test_work_run_all_passed()
        work = Work()
        work.draft = self.draft
        work.workId = "testWork2"
        work.path = currentdir
        self.assertTrue(work.property_is_ready())
        work_path = os.path.join(currentdir, "ta", "work.json")
        self.assertFalse(work.create())

    def test_property_not_ready(self):
        work = Work()
        # work.draft = self.draft
        work.workId = "testWork2"
        work.path = currentdir
        self.assertFalse(work.property_is_ready())
        work = Work()
        work.draft = self.draft
        # work.workId = "testWork2"
        work.path = currentdir
        self.assertFalse(work.property_is_ready())
        work = Work()
        work.draft = self.draft
        work.workId = "testWork2"
        # work.path = currentdir
        self.assertFalse(work.property_is_ready())

    def tearDown(self) -> None:
        shutil.rmtree(os.path.join(currentdir, "ta"))

if __name__ == "__main__":
    unittest.main()