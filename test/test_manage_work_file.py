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
        path_draft = os.path.join(self.path_ta,"draft.json")
        DirManagement.create_dir(self.path_ta)
        
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
        # Create ta/draft.json
        with open(path_draft,"w") as file:
            json.dump(self.draft,file)
            file.close()
        
        # Init test file
        listname = ["test_1.txt","test_2.txt","test_3.txt"]
        test_data = "123456"
        # Create test file
        for filename in listname:
            with open(os.path.join(currentdir,filename),"w") as file:
                json.dump(test_data,file)
                file.close()
        # Zip test file
        self.path_target = os.path.join(currentdir,"631055555_hi_ex1.zip")
        with zipfile.ZipFile(self.path_target,"w") as my_zip:
            text_1 = os.path.join(currentdir,"test_1.txt")
            text_2 = os.path.join(currentdir,"test_2.txt")
            text_3 = os.path.join(currentdir,"test_3.txt")
            my_zip.write(text_1,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_2,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_3,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.close()

        for filename in listname:
            os.remove(os.path.join(currentdir,filename))
        return super().setUp()

    def test_extract(self):
        manage_work_file(currentdir,self.draft)
        listfile = os.listdir(currentdir)
        self.assertIn("631055555_hi_ex1.zip",listfile)
    
    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path_ta)
        os.remove(os.path.join(currentdir,"631055555_hi_ex1.zip"))
        path_folder = os.path.join(currentdir,"631055555_hi_ex1")
        DirManagement.remove_dir(path_folder)
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()