"""
Author Vitvara

### This libary is about manage file and directory you can import those module to use by

from file_management_lib import module name

### if you want to use only 1 method you can do it by

method = Object().method
method(parameter)

### or if you use more than 1 method you should create an variable to keep those Object

object1 = Object1()

object1.method1()
object1.method2(parameter)

### to be clear about those parameter
### `path` on window path can't directly use by themself you need to add r in font of the path string to avoid backslash error
r"this\is\path" 
### in DirManagement you should put directory name that you want in to the back of the path
r"this\is\path\dirname" 

### anyone whio uses macOS, please give me some information that what is the format of the path ###

### `filename` need to be filename and its extension and have backslash in front of file name
r"\filename.txt"
r"\filename.json"

### if there is anything in doubt, you can mention me in discord
"""

import os
import shutil

class FileEditor:
    @staticmethod
    def create_file(path: str, filename: str) -> None:
        with open(path+filename, 'w') as fp:
            pass

    @staticmethod
    def delete_file(path: str,filename: str) -> bool:
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

"""
Author vitvara
=================================================================================================================
work editor is about work.json
its have method that can edit work.json and it already handle case that not have work.json or already have work.json
path need to be ta dir

example use:
### init work.json
work = WorkEditor(r"\this\is\path)
// it will autometic create work.json and read draft.json (if you want to use this module make sure that you check draft.json that already exits)
### get work.json
filework = work.read_file(r"\work.json") -> dict
### writting work.json
work.write_work({'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'})
"""
import os 
import json

class WorkEditor(FileEditor):
    def __init__(self,path : str) -> None:
        """
        create draft.json on ta dir when its not exits
        and create work.json

        Args:
            path (str): path of ta directory
        """
        self.path = path
    
    def init_work(self) -> None:
        self.create_file(self.path,"\work.json")
        with open(self.path+"\work.json", 'w') as outfile:
            json.dump({"run_work":[]}, outfile)
            outfile.close()

    def create_file_work(self) -> bool:
        if not os.path.exists(self.path+"\work.json"):
            self.init_work()
            print(self.path+r"\work.json created")
            return True
        else:
            print(self.path+r"\work.json exits")
            return False

    def write_work(self, stu_data : dict) -> bool:
        """add student data to work.json

        Args:
            stu_data (list): list of student data (should ordered)

        Returns:
            bool: if the stu_data does not match with draft.json return False else True
        """
        with open(self.path+"\work.json", "r+") as file:
            data = json.load(file)
            data["run_work"].append(stu_data)
            file.seek(0)
            json.dump(data, file,indent = 2)
            print(str(stu_data) + " has been written down in "+ self.path + r"\work.json")
            file.close()

    def read_file(self,name : str) -> dict:
        with open(self.path+name) as f:
            data = json.load(f)

        return data
if __name__ == "__main__":
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    rootdir = os.path.dirname(os.path.dirname(currentdir))
    DirManagement().create_dir(rootdir+r"\ta")
    print(rootdir)
    work = WorkEditor(rootdir+r"\ta")
    stu_data = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'}
    work.create_file_work()
    work.write_work(stu_data)
