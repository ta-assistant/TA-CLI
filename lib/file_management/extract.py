import os
import zipfile
from file_management_lib import DirManagement

def list_file(path):
    listfile = os.listdir(path)
    return listfile

def unzipfile(listfile):
    create_dir = DirManagement().create_dir
    for i in listfile:
        if ".zip" in i :
            name = path + f"/{i}"
            folder = name[0:-4]
            with zipfile.ZipFile(name) as my_zip:
                create_dir(folder)
                my_zip.extractall(folder)
                my_zip.close()

path = "C:/Users/detec/Documents/Grid"
listfile = list_file(path)
unzipfile(listfile)
    