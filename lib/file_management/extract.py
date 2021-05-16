"""
Author Paranchai

### This function is about extract only the ".zip" files you can use these method by

unzipfile(path: str)

### if have any suggestions or problem, you can direct message to me
"""

import os
import zipfile
from file_management_lib import DirManagement

def unzipfile(path: str):
    """
    ###'path: str' is directory name that you want this function to extract files and create folders in this
    ### You should to change backslash to sla for prevebt backslash error
    """
    listfile = os.listdir(path)
    create_dir = DirManagement().create_dir
    for i in listfile:
        if ".zip" in i :
            name = path + f"/{i}"
            folder = name[0:-4]
            with zipfile.ZipFile(name) as my_zip:
                create_dir(folder)
                my_zip.extractall(folder)
                my_zip.close()
                print(f"Successfully extracted files to {folder}" )

if __name__ ==  "__main__" :
    path = "C:/Users/detec/Documents/Grid"
    unzipfile(path)
    