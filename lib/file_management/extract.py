"""
Author Paranchai

### This function is about extract only the ".zip" files you can use these method by

unzipfile(path: str)

### if have any suggestions or problem, you can direct message to me
"""

import os
import zipfile
from file_management_lib import DirManagement, WorkEditor


def check_filename_draft(filename: list,draft: list) -> bool:
    if len(filename) != len(draft):
        return False
    else:
        return True

def check_valid_filename(path: str,filename: str) -> bool:
    """check that zip filename is valid or not

    Args:
        path (str): path of work directory
        filename (str): zip file name

    Returns:
        bool: if zip file name is valid return true else false
    """
    fdraft_path = os.path.join(path,"ta","draft.json")
    fdraft = WorkEditor("").read_file(fdraft_path)
    fdraft = fdraft["fileDraft"]
    key=[]
    reminder = ""
    prejob = {}
    for i in fdraft:
        if i == "{":
            reminder = ""
        elif i == "}":
            key.append(reminder)
        else:
            reminder += i
    list_filename = filename.split("_")
    if not check_filename_draft(list_filename,key):
        print("Invalid file name " + filename)
        return False
    else:
        return True

def unzipfile(path: str):
    """
    'path: (str)' is directory name that you want this function to extract files and create folders in this
    You should to change backslash to sla for prevebt backslash error
    The floder's name where files extracted is same as the zip file's name.
    """
    listfile = os.listdir(path)
    create_dir = DirManagement().create_dir
    for i in listfile:
        if ".zip" in i :
            name = os.path.join(path, f"/{i}")
            folder = name[0:-4]
            if check_valid_filename(path,folder):
                with zipfile.ZipFile(name) as my_zip:
                    create_dir(folder)
                    my_zip.extractall(folder)
                    my_zip.close()
                    print(f"Successfully extracted files to {folder}")


