import unittest
import os,sys,inspect
import zipfile
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from lib.file_management.file_management_lib import FileEditor, DirManagement, WorkEditor

# #create file
# method = FileEditor().create_file
# method(currentdir,r"\test_1.txt")
# method(currentdir,r"\test_2.txt")

# #zip file
# os.chdir(currentdir)
# target = currentdir + "\\631055555_hi_ex1.zip"
# with zipfile.ZipFile(target,"w") as my_zip:
#     my_zip.write("test_1.txt",compress_type=zipfile.ZIP_DEFLATED)
#     my_zip.write("test_2.txt",compress_type=zipfile.ZIP_DEFLATED)
#     my_zip.close()

path_ta = os.path.join(currentdir,"ta")
DirManagement.create_dir(path_ta)

FileEditor.create_file(path_ta,"draft.json")
path_draft = os.path.join(path_ta,"draft.json")
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

DirManagement().remove_dir(path_ta)





# #unzip file (test)
# os.chdir(parentdir+r"/lib/file_management")
# sys.path.insert(0,os.getcwd())

# from lib.file_management import extract
# extract.unzipfile(currentdir)

# #check file 
# target = currentdir + "\\631055555_hi_ex1"
# listfile = os.listdir(target)

# if "test_1.txt" in listfile and "test_2.txt" in listfile :
#     print("Success")

# #delete file
# FileEditor.delete_file(currentdir,r"\test_1.txt")
# FileEditor.delete_file(currentdir,r"\test_2.txt")
# FileEditor.delete_file(currentdir,r"\\631055555_hi_ex1.zip")
# DirManagement.remove_dir(currentdir + r"\\631055555_hi_ex1")

#if __name__ == '__main__':
#    unittest.main()