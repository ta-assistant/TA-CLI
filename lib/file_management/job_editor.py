from file_management_lib import FileEditor
import os 
import json

class JobEditor(FileEditor):
    def __init__(self,path : str) -> None:
        self.path = path
        if os.path.exists(self.path+"draft.json"):
            self.draft = self.read_file("draft.json")["output_draft"]
        else:
            pass
        self.create_file_job()

    def create_file_job(self):
        if not os.path.exists(self.path+"job.json"):
            self.create_file(self.path,"job.json")
            with open(self.path+"job.json", 'w') as outfile:
                json.dump({"run_job":[]}, outfile)
                outfile.close()
            print("job.json created")
        else:
            print("job.json exits")

    def write_job(self, stu_data : list) -> bool:
        if len(self.draft) != len(stu_data):
            return False
        store = {}
        for key,stu_data in zip(self.draft,stu_data):
            store[key] = stu_data
        with open(self.path+"job.json", "r+") as file:
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
    job = JobEditor(r"C:\Users\Admin\Desktop\ex1\ta\\")
    stu_data = ["6310546066", "vitvara", "ex1", "12", "13", "nice job"]
    print(job.write_job(stu_data))

