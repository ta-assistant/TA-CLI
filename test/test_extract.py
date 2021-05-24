import unittest
import os,sys,inspect
import zipfile
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
filemanagedir = os.path.join(parentdir,"lib","file_management")
sys.path.insert(0,parentdir)

from lib.file_management.file_management_lib import FileEditor, DirManagement, WorkEditor
from lib.file_management import extract

class TestExtract(unittest.TestCase):
    def setUp(self) -> None:
        self.path_ta = os.path.join(currentdir,"ta")
        DirManagement.create_dir(self.path_ta)

        FileEditor.create_file(self.path_ta,"draft.json")
        path_draft = os.path.join(self.path_ta,"draft.json")
        draft = {
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
        with open(path_draft,"r+") as file:
            json.dump(draft,file)
            file.close()

        create_file = FileEditor().create_file
        create_file(currentdir,"test_1.txt")
        create_file(currentdir,"test_2.txt")

        self.path_target = os.path.join(currentdir,"631055555_hi_ex1.zip")
        with zipfile.ZipFile(self.path_target,"w") as my_zip:
            text_1 = os.path.join(currentdir,"test_1.txt")
            text_2 = os.path.join(currentdir,"test_2.txt")
            my_zip.write(text_1,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_2,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.close()
        FileEditor.delete_file(currentdir,"test_1.txt")
        FileEditor.delete_file(currentdir,"test_2.txt")

        return super().setUp()

    def test_extract(self):
        extract.unzipfile(currentdir)
        listfile = os.listdir(currentdir)
        self.assertIn("631055555_hi_ex1",listfile)
    
    def tearDown(self) -> None:
        DirManagement.remove_dir(self.path_ta)
        FileEditor.delete_file(currentdir,"631055555_hi_ex1.zip")
        path_folder = os.path.join(currentdir,"631055555_hi_ex1")
        DirManagement.remove_dir(path_folder)
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()