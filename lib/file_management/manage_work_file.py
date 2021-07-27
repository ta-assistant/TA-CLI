"""
Author Paranchai
### This function is about extract only the ".zip" files you can use these method by
unzipfile(path: str)
### if have any suggestions or problem, you can direct message to me
"""

from typing import Counter
import zipfile
import shutil
import os

from .file_management_lib import DirManagement
from .loadin_bar import progressBar
from lib.cli_displayed import display_status_symbol

# private

def _check_extension(draft):
    remainder = ""
    for i in draft["fileDraft"][::-1]:
        # Find `.` on filename and extract the extension then return it.
        if i == ".":
            extension = (remainder + i)[::-1]
            break
        remainder += i
    return extension

def _check_draft_file(draft):
    key = []
    # Loop find key
    for i in draft["fileDraft"]:
        # Reset remainder
        if i == "{":
            remainder = ""
        # Append remainder to list(key)
        elif i == "}":
            key.append(remainder)
        # Add keys letter to remainder
        else:
            remainder += i
    return key

def _check_file_name(filename,draft):
    # Get extension from draft
    extension = _check_extension(draft)
    # Is filename's extension follow draft's extension?
    if extension not in filename:
        return False
    # Remove extension from filename and split _ into a list
    list_filename = filename[:-len(extension)].split("_")
    # Get key from draft
    list_draft = _check_draft_file(draft)
    # A studentId need to be integer
    for key,value in zip(list_draft,list_filename):
        if key == "studentId":
            try:
                int(value)
            except ValueError:
                return False
    return True
    
def _move_stu_file(path,filename):
    # Remove filename extension
    dirname = _remove_extension(filename)
    # Check that filename is already moved or not
    if os.path.exists(os.path.join(path,"ta","Assignment",dirname,filename)):
        return False
    # Create dir to keep a student file
    DirManagement().create_dir(os.path.join(path,"ta","Assignment",dirname),out=False)
    # Copy and paste student file in Assuginment dir.
    shutil.copyfile(os.path.join(path,filename),os.path.join(path,"ta","Assignment",dirname,filename))
    return True

def _check_valid_file_name(draft,listfile):
    # Check that filename is folow draft or not
    validfile = []
    for i in listfile[::]:
        if not _check_file_name(i,draft):
            listfile.remove(i)
            # Remove ta dir from list file
            if i != "ta":
                validfile.append(i)
    return validfile

def _remove_extension(filename):
    countname = 0
    for char in filename[::-1]:
            countname += 1
            if char == ".":
                dirname = filename[:-countname]
                break
    return dirname

def _unzip(folder,name):
    with zipfile.ZipFile(name) as my_zip:
        # extract to Assignment dir
        try:
            DirManagement().create_dir(folder,out=False)
            my_zip.extractall(folder)
            my_zip.close()
            return 1
        # Broken zip file
        except (IOError, zipfile.BadZipfile) as e:
            out= " "*100
            print(f"\rBad zip file given as {name}.{out}\n")
            shutil.rmtree(folder)
            return 0

        
# public

def manage_work_file(path: str, draft: dict):
    """
    Create Assignment directory in ta dir and check student filename that are folow draft or not is 
    it's so copy them to Assignment directory (In case it's a zip it will automatic extract that file if the 
    fileDraft extension is a .zip)

    Parameter
    -----------
    path: string
        path of working directory
    
    draft: dict
        dictionary of draft
        include fileDraft and outputDraft

    Return
    -------
    Boolean:
        True when it's can process some file into Assignment dir 
        False when no file are follow the draft_state
    
    Example
    ---------
    Case1:
        dir2 tree
        |-- 123456789.zip
        |-- 123456788.zip
        |-- 123456787.zip
        |-- 123456786.zip
        |__ ta/

        >>> path = "/root/dir1/dir2"
        >>> draft = {'outputDraft': ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp'], 'fileDraft': '{studentId}_test.zip'}
        >>> manage_work_file(path, draft)
        ... |-[/] 4 file has processed
        ... True

    Result:
        dir2\ta tree
            |-- Assignment
                    |-- 123456789/
                    |-- 123456788/
                    |-- 123456787/
                    |__ 123456786/

    Case2:
        dir2 tree
        |-- 123456789.py
        |-- 123456788.py
        |-- 123456787.py
        |-- 123456786.py
        |__ ta/
        
        >>> path = "/root/dir1/dir2"
        >>> draft = {'outputDraft': ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp'], 'fileDraft': '{studentId}_test.zip'}
        >>> manage_work_file(path, draft)
        ... |-[/] 0 file has processed
        ... False
    
    Result:
        dir2\ta tree
            |__ Assignment/

    """
    create_dir = DirManagement().create_dir
    listfile = os.listdir(path)
    
    validfile = _check_valid_file_name(draft,listfile)
    num_valid_file = len(validfile)
    
    # Have an invalid filename
    if num_valid_file != 0:
        display_status_symbol(1,1,"Valid file: (not include on scoring process)")
        # Displayed invalid filename
        count = 0
        end = False

        for i in validfile:
            count += 1
            if count == num_valid_file:
                end = True
            display_status_symbol(2,2,i,end)
        # No file are follow the draft
        if len(listfile) == 0:
            return False

    # Create Assignment directory
    create_dir(os.path.join(path,"ta","Assignment"),out=False)

    # Loop check file one by one
    count = 0
    for filename in progressBar(listfile,prefix = 'progress:', suffix = 'complete ', length = 20):
        name = os.path.join(path, f"{filename}")
        dirname =  _remove_extension(filename)
        Assignment_folder = os.path.join(path, "ta","Assignment",f"{dirname}")
        # Unzip in Assignment directory
        if ".zip" in filename:
            if os.path.exists(Assignment_folder):
                continue
            count +=  _unzip(Assignment_folder,name)

        # Move file to Assignment directory
        else:
            if _move_stu_file(path,filename):
                count += 1

    # Displayed processed file
    print("     "*20,end="\r")
    if count == 0:
        display_status_symbol(1,1,f"{count} file has processed")
    else:
        display_status_symbol(1,0,f"{count} file has processed")
    return True