"""
Author Vitvara

# This libary is about manage file and directory you can import those module to use by

from file_management_lib import module name

# if you want to use only 1 method you can do it by

method = Object().method
method(parameter)

# or if you use more than 1 method you should create an variable to keep those Object

object1 = Object1()

object1.method1()
object1.method2(parameter)

# to be clear about those parameter
# `path` on window path can't directly use by them self you need to add r in font of the path string to avoid backslash error
r"this\is\path" 
# in Dirmanagement you should put directory name that you want in to the back of the path
r"this\is\path\dirname" 

### anyone whio uses macOS, please give me some information that what is the format of the path ###

# `filename` need to be filename and its extension and have backslash in front of file name
r"\filename.txt"
r"\filename.json"

# if there is anything in doubt, you can mention me in discord
"""

import os
import shutil

class FileEditor:
    @staticmethod
    def create_file(path: str, filename: str) -> None:
        with open(path+filename, 'w') as fp:
            pass

    @staticmethod
    def delete_file(path:str,filename:str) -> bool:
        if os.path.exists(path+filename):
            os.remove(path+filename)
            return True
        else:
            print("The "+path+filename+" does not exist")
            return False

    @staticmethod
    def read_file(path: str, filename: str) -> None:
        pass


class DirManagement:
    @staticmethod
    def create_dir(path: str) -> None:
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
            return False
        else:
            print ("Successfully created the directory %s " % path)
            return True
        
    @staticmethod
    def remove_dir(path: str) -> None:
        try:
            shutil.rmtree(path)
        except OSError:
            print ("Deletion of the directory %s failed" % path)
            return False
        else:
            print ("Successfully deleted the directory %s" % path)
            return True
                