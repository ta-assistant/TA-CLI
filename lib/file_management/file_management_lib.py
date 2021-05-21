import os
import shutil

class FileEditor:
    @staticmethod
    def create_file(path: str, filename: str) -> None:
        file_path = os.path.join(path,filename)
        with open(file_path, 'w') as fp:
            pass

    @staticmethod
    def delete_file(path: str,filename: str) -> bool:
        file_path = os.path.join(path,filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            print("The "+file_path+" does not exist")
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


import os 
import json

class WorkEditor(FileEditor):
    def __init__(self,path : str,workId=None) -> None:
        """
        create draft.json on ta dir when its not exits
        and create work.json

        Args:
            path (str): path of ta directory
        """
        self.path = path
        self.work_path = os.path.join(self.path,"work.json")
        self.draft = "N/A"
        self.workId = workId

    def add_draft(self):
        self.draft = self.read_file(os.path.join(self.path,"ta"),"draft.json")["workDraft"]

    def init_work(self) -> None:
        self.create_file(self.path,"work.json")
        with open(self.work_path, 'w') as outfile:
            json.dump({"workId":str(self.workId),"workDraft":self.draft,"scores":[]}, outfile)
            outfile.close()

    def create_file_work(self) -> bool:
        if not os.path.exists(self.work_path):
            self.init_work()
            print(self.work_path+"work.json created")
            return True
        else:
            print(self.work_path+"work.json exits")
            return False

    def write_work(self, stu_data : dict) -> bool:
        """add student data to work.json

        Args:
            stu_data (list): list of student data (should ordered)

        Returns:
            bool: if the stu_data does not match with draft.json return False else True
        """
        with open(self.work_path, "r+") as file:
            data = json.load(file)
            data["scores"].append(stu_data)
            file.seek(0)
            json.dump(data, file,indent = 2)
            print(str(stu_data) + " has been written down in "+ self.work_path)
            file.close()


    def read_file(self,name : str) -> dict:
        file_path = os.path.join(self.path,name)
        with open(file_path) as f:
            data = json.load(f)

        return data
if __name__ == "__main__":
    import os,sys,inspect
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    rootdir = os.path.dirname(os.path.dirname(currentdir))
    ta = os.path.join(rootdir,"ta")
    print(ta)
    work_path = os.path.join(ta,"work.json")
    DirManagement().create_dir(ta)
    print(rootdir)
    work = WorkEditor(ta,123456)
    work.create_file_work()
    print(work.read_file(work_path))
    stu_data = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'}
    work.create_file_work()
    work.write_work(stu_data)
    print()
    print(work.read_file(work_path))
