"""
Author vitvara
=================================================================================================================
work editor is about work.json
its have method that can edit work.json and it already handle case that not have work.json or already have work.json
path need to be ta dir
"""

from file_management_lib import FileEditor, DirManagement
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
        if os.path.exists(self.path+r"\draft.json"):
            self.draft = self.read_file(r"\draft.json")["output_draft"]
            print("read draft.json on "+self.path+r"\draft.json")
        else:
            self.draft = None

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

    def write_work(self, stu_data : list) -> bool:
        """add student data to work.json

        Args:
            stu_data (list): list of student data (should ordered)

        Returns:
            bool: if the stu_data does not match with draft.json return False else True
        """
        if len(self.draft) != len(stu_data):
            print("draft.json dosen't match with student data please try again")
            return False
        store = {}
        for key,stu_data in zip(self.draft,stu_data):
            store[key] = stu_data
        with open(self.path+"\work.json", "r+") as file:
            data = json.load(file)
            data["run_work"].append(store)
            file.seek(0)
            json.dump(data, file,indent = 2)
            print(str(store) + " has been written down in "+ self.path + r"\work.json")

        return True

    def read_file(self,name : str) -> dict:
        with open(self.path+name) as f:
            data = json.load(f)

        return data

if __name__ == "__main__":
    work = WorkEditor(r"C:\Users\Admin\Desktop\ex1\ta")
    stu_data = ["6310546066", "vitvara", "ex1", "12", "13", "nice work"]
    work.create_file_work()
    print(work.write_work(stu_data))

