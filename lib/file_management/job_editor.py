"""
Author vitvara
=================================================================================================================
Job editor is about job.json
its have method that can edit job.json and it already handle case that not have job.json or already have job.json
path need to be ta dir
"""

from file_management_lib import FileEditor
import os 
import json

class JobEditor(FileEditor):
    def __init__(self,path : str) -> None:
        self.path = path
        if os.path.exists(self.path+"\draft.json"):
            self.draft = self.read_file("\draft.json")["output_draft"]
        else:
            pass
        self.create_file_job()

    def init_job(self) -> None:
        self.create_file(self.path,"\job.json")
        with open(self.path+"\job.json", 'w') as outfile:
            json.dump({"run_job":[]}, outfile)
            outfile.close()

    def create_file_job(self) -> None:
        if not os.path.exists(self.path+"\job.json"):
            self.init_job()
            print("job.json created")
        else:
            print("job.json exits")

    def write_job(self, stu_data : list) -> bool:
        """write job.json

        Args:
            stu_data (list): list of student data (should ordered)

        Returns:
            bool: if the stu_data does not match with draft.json return False else True
        """
        if len(self.draft) != len(stu_data):
            return False
        store = {}
        for key,stu_data in zip(self.draft,stu_data):
            store[key] = stu_data
        with open(self.path+"\job.json", "r+") as file:
            data = json.load(file)
            data["run_job"].append(store)
            print(data)
            file.seek(0)
            json.dump(data, file,indent = 2)
        return True

    def read_file(self,name : str) -> dict:
        with open(self.path+name) as f:
            data = json.load(f)

        return data

if __name__ == "__main__":
    job = JobEditor(r"C:\Users\Admin\Desktop\ex1\ta")
    stu_data = ["6310546066", "vitvara", "ex1", "12", "13", "nice job"]
    print(job.write_job(stu_data))

