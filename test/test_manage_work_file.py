import unittest
import os,sys,inspect
import zipfile
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

from lib.file_management import DirManagement
from lib.file_management import manage_work_file

class TestExtract(unittest.TestCase):
    def setUp(self) -> None:
        self.path_ta = os.path.join(currentdir,"ta")
        DirManagement.create_dir(self.path_ta)
        
        self.draft_zip = {
            "fileDraft": "{student_id}.zip",
            "outputDraft": [
            "student_id",
            "name",
            "ex",
            "score1",
            "score2",
            "comment"
            ]
        }
        self.draft_py = {
            "fileDraft": "{student_id}.py",
            "outputDraft": [
            "student_id",
            "name",
            "ex",
            "score1",
            "score2",
            "comment"
            ]
        }

    def add_draft(self,draft):
        # Create ta/draft.json
        path_draft = os.path.join(self.path_ta,"draft.json")
        with open(path_draft,"w") as file:
            json.dump(draft,file)
            file.close()
        return super().setUp()

    def create_zip(self,name):
        # Init test file
        listname = ["test_1.txt","test_2.txt","test_3.txt"]
        test_data = "123456"
        # Create test file
        for filename in listname:
            with open(os.path.join(currentdir,filename),"w") as file:
                json.dump(test_data,file)
                file.close()
        # Zip test file
        self.path_target = os.path.join(currentdir,f"{name}.zip")
        with zipfile.ZipFile(self.path_target,"w") as my_zip:
            text_1 = os.path.join(currentdir,"test_1.txt")
            text_2 = os.path.join(currentdir,"test_2.txt")
            text_3 = os.path.join(currentdir,"test_3.txt")
            my_zip.write(text_1,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_2,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_3,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.close()

        for filename in listname:
            # remove text file
            os.remove(os.path.join(currentdir,filename))
        
    def create_py_file(self):
        test_data = "123456"
        # Create test file
        listname = [f"100056{i}.py" for i in range(100)]
        for filename in listname:
            with open(os.path.join(currentdir,filename),"w") as file:
                json.dump(test_data,file)
                file.close()

    def test_extract_zip(self):
        # add draft
        self.add_draft(self.draft_zip)
        # create zip file
        for i in range(100):
            self.create_zip(f"100000254{i}")
        manage_work_file(currentdir,self.draft_zip)
        listdir = os.listdir(os.path.join(currentdir,"ta","Assignment"))
        listfile = os.listdir(currentdir)
        for i in range(100):
            self.assertIn(f"100000254{i}",listdir)
            self.assertIn(f"100000254{i}.zip",listfile)
        
        # remove original zip file
        for i in range(100):
            os.remove(os.path.join(currentdir,f"100000254{i}.zip"))

    def test_manage_work_py(self):
        # ad draft
        self.add_draft(self.draft_py)
        # create python file
        self.create_py_file()
        manage_work_file(currentdir,self.draft_py)
        listassign = os.listdir(os.path.join(currentdir,"ta","Assignment"))
        listcurrent = os.listdir(os.path.join(currentdir))
        # check that file.py that are created is copy to Assignment dir
        listname = [f"100056{i}" for i in range(100)]
        for dir in listname:
            self.assertTrue(dir in listassign)
            self.assertTrue(f"{dir}.py" in listcurrent)
            os.remove(os.path.join(currentdir,f"{dir}.py"))

    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path_ta)
        path_folder = os.path.join(currentdir,"631055555_hi_ex1")
        DirManagement.remove_dir(path_folder)
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()