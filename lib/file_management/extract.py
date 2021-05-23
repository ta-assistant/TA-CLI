"""
Author Paranchai
### This function is about extract only the ".zip" files you can use these method by
unzipfile(path: str)
### if have any suggestions or problem, you can direct message to me
"""

import zipfile
from lib.file_management.file_management_lib import DirManagement, WorkEditor, FileEditor
import inspect
import sys
import os


def unzipfile(path: str):
    """
    'path: (str)' is directory name that you want this function to extract files and create folders in this
    You should to change backslash to sla for prevebt backslash error
    The floder's name where files extracted is same as the zip file's name.
    """
    listfile = os.listdir(path)
    create_dir = DirManagement().create_dir
    for filename in listfile:
        if ".zip" in filename:
            name = os.path.join(path, f"{filename}")
            folder = name[0:-4]
            with zipfile.ZipFile(name) as my_zip:
                create_dir(folder)
                my_zip.extractall(folder)
                my_zip.close()
                print(f"Successfully extracted files to {folder}")
            FileEditor.delete_file(path, filename)