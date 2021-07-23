"""
Author Paranchai
### This function is about extract only the ".zip" files you can use these method by
unzipfile(path: str)
### if have any suggestions or problem, you can direct message to me
"""
import zipfile
from lib.file_management.file_management_lib import DirManagement, WorkEditor, FileEditor
from lib.file_management.loadin_bar import progressBar
from lib.file_management.check_valid_filename import check_file_name
import shutil
import os


def move_stu_file(path,filename):
    count = 0
    for char in filename[::-1]:
        count += 1
        if char == ".":
            dirname = filename[:-count]
            break
    if os.path.exists(os.path.join(path,"ta","Assignment",dirname,filename)):
        return False
    DirManagement().create_dir(os.path.join(path,"ta","Assignment",dirname),out=False)
    shutil.copyfile(os.path.join(path,filename),os.path.join(path,"ta","Assignment",dirname,filename))
    return True

def unzipfile(path: str,draft):
    """
    'path: (str)' is directory name that you want this function to extract files and create folders in this
    You should to change backslash to sla for prevebt backslash error
    The floder's name where files extracted is same as the zip file's name.
    """
    listfile = os.listdir(path)
    validfile = []
    for i in listfile[::]:
        if not check_file_name(path,i,draft):
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
    create_dir(os.path.join(path,"ta","Assignment"),out=False)
    for filename in progressBar(listfile,prefix = 'progress:', suffix = 'complete ', length = 20):
        name = os.path.join(path, f"{filename}")
        countname = 0
        for char in filename[::-1]:
            countname += 1
            if char == ".":
                dirname = filename[:-countname]
                break
        
        folder = os.path.join(path, "ta","Assignment",f"{dirname}")
        if ".zip" in filename:
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
        else:
            if move_stu_file(path,filename):
                count += 1

    print("     "*20,end="\r")
    print(" |")
    print(f" |-[/] {count} file has processed")
    return True