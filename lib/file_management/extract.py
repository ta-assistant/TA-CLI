"""
Author Paranchai
### This function is about extract only the ".zip" files you can use these method by
unzipfile(path: str)
### if have any suggestions or problem, you can direct message to me
"""

import zipfile
from lib.file_management.file_management_lib import DirManagement, WorkEditor, FileEditor
from lib.file_management.loadin_bar import progressBar
import inspect
import sys
import shutil
import os


def unzipfile(path: str):
    """
    'path: (str)' is directory name that you want this function to extract files and create folders in this
    You should to change backslash to sla for prevebt backslash error
    The floder's name where files extracted is same as the zip file's name.
    """
    listfile = os.listdir(path)
    if "ta" in listfile:
        listfile.remove("ta")
    create_dir = DirManagement().create_dir
    out= " "*100
    for filename in progressBar(listfile,prefix = 'Unzip progress:', suffix = 'complete ', length = 20):
        if ".zip" in filename:
            name = os.path.join(path, f"{filename}")
            folder = os.path.join(path, "ta","extract",f"{filename}")[:-3]
            with zipfile.ZipFile(name) as my_zip:
                try:
                    create_dir(folder,out=False)
                    my_zip.extractall(folder)
                    my_zip.close()
                except (IOError, zipfile.BadZipfile) as e:
                    print(f"\rBad zip file given as {name}.{out}\n")
                    shutil.rmtree(folder)
