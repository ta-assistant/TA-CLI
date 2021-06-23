"""
Author Paranchai
### This function is about extract only the ".zip" files you can use these method by
unzipfile(path: str)
### if have any suggestions or problem, you can direct message to me
"""

from typing import Counter
import zipfile
from lib.file_management.file_management_lib import DirManagement, WorkEditor, FileEditor
from lib.file_management.loadin_bar import progressBar
from lib.file_management.check_valid_filename import check_file_name
import sys
import shutil
import os
import time
    
def unzipfile(path: str):
    """
    'path: (str)' is directory name that you want this function to extract files and create folders in this
    You should to change backslash to sla for prevebt backslash error
    The floder's name where files extracted is same as the zip file's name.
    """
    listfile = os.listdir(path)
    validfile = []
    for i in listfile[::]:
        if not check_file_name(path,i):
            listfile.remove(i)
            if i != "ta":
                validfile.append(i)
    if len(validfile) != 0:
        print(" |-[x] Valid file: (not include in scoring process)")
        for i in validfile: print(" |   |-[*]",i)
        if len(listfile) == 0:
            return False
    create_dir = DirManagement().create_dir
    out= " "*100
    count = 0
    for filename in progressBar(listfile,prefix = 'Unzip progress:', suffix = 'complete ', length = 20):
        if ".zip" in filename:
            name = os.path.join(path, f"{filename}")
            folder = os.path.join(path, "ta","extract",f"{filename}")[:-3]
            if os.path.exists(folder):
                continue
            with zipfile.ZipFile(name) as my_zip:
                try:
                    create_dir(folder,out=False)
                    my_zip.extractall(folder)
                    my_zip.close()
                    count += 1
                except (IOError, zipfile.BadZipfile) as e:
                    print(f"\rBad zip file given as {name}.{out}\n")
                    shutil.rmtree(folder)
    print("     "*20,end="\r")
    print(" |")
    print(f" |-[/] {count} file has been extracted")
    return True