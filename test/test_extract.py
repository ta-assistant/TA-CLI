import unittest
import os,sys,inspect
import zipfile

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from lib.file_management import file_management_lib

#create file
method = file_management_lib.FileEditor().create_file
method(currentdir,r"\test_1.txt")
method(currentdir,r"\test_2.txt")

#zip file
os.chdir(currentdir)
target = currentdir + "\\631055555_hi_ex1.zip"
with zipfile.ZipFile(target,"w") as my_zip:
    my_zip.write("test_1.txt",compress_type=zipfile.ZIP_DEFLATED)
    my_zip.write("test_2.txt",compress_type=zipfile.ZIP_DEFLATED)
    my_zip.close()


#unzip file (test)
os.chdir(parentdir+r"/lib/file_management")
sys.path.insert(0,os.getcwd())

from lib.file_management import extract
extract.unzipfile(currentdir)

#check file 
target = currentdir + "\\631055555_hi_ex1"
listfile = os.listdir(target)

if "test_1.txt" in listfile and "test_2.txt" in listfile :
    print("Success")

#delete file
file_management_lib.FileEditor.delete_file(currentdir,r"\test_1.txt")
file_management_lib.FileEditor.delete_file(currentdir,r"\test_2.txt")
file_management_lib.FileEditor.delete_file(currentdir,r"\\631055555_hi_ex1.zip")
file_management_lib.DirManagement.remove_dir(currentdir + r"\\631055555_hi_ex1")



#if __name__ == '__main__':
#    unittest.main()