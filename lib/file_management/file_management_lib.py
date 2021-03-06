import json
import os
import shutil


class FileEditor:
    @staticmethod
    def create_file(path: str, filename: str) -> None:
        file_path = os.path.join(path, filename)
        with open(file_path, 'w') as fp:
            pass

    @staticmethod
    def delete_file(path: str, filename: str) -> bool:
        file_path = os.path.join(path, filename)
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
    def create_dir(path: str, out=True) -> None:
        try:
            os.mkdir(path)
        except OSError:
            if out:
                print("Creation of the directory %s failed" % path)
            return False
        else:
            if out:
                print("Successfully created the directory %s " % path)
            return True
    @staticmethod
    def remove_dir(path: str) -> None:
        try:
            shutil.rmtree(path)
        except OSError:
            print("Deletion of the directory %s failed" % path)
            return False
        else:
            print("Successfully deleted the directory %s" % path)
            return True


class WorkEditor(FileEditor):
    def init_work(self, path) -> None:
        self.create_file(os.path.join(path, "ta"), "work.json")
        with open(os.path.join(path, "ta", "work.json"), 'w') as outfile:
            json.dump({"workId": "N/A", "workDraft": "N/A",
                       "scores": []}, outfile)
            outfile.close()

    def check_exits_work(self, path):
        if os.path.exists(os.path.join(path, "ta", "work.json")):
            return True
        else:
            return False

    def create_file_work(self, path, workId, draft) -> bool:
        if not self.check_exits_work(path):
            self.init_work(path)
            self.add_workid(path, workId)
            self.add_draft(path, draft)
            return True
        else:
            if self.check_work_draft(path,draft):
                while True:
                    if not os.path.exists(os.path.join(path,"ta","work.json")):
                        self.create_file_work()
                        break
            return False

    def write_work(self, path, stu_data: dict) -> bool:
        """add student data to work.json
        Args:
            stu_data (list): list of student data (should ordered)
        Returns:
            bool: if the stu_data does not match with draft.json return False else True
        """
        with open(os.path.join(path, "ta", "work.json"), "r+") as file:
            data = json.load(file)
            data["scores"].append(stu_data)
            file.seek(0)
            json.dump(data, file, indent=2)
            print(str(stu_data) + " has been written down in " +
                  os.path.join(path, "ta", "work.json"))
            file.close()

    def add_workid(self, path, workId):
        if self.check_exits_work(path):
            with open(os.path.join(path, "ta", "work.json"), "r") as file:
                data = json.load(file)
                file.close()
            with open(os.path.join(path, "ta", "work.json"), "w") as file:
                data["workId"] = str(workId)
                json.dump(data, file)
                file.close()
            print(f" |-[*] Your workId is \'{workId}\'")

    def add_draft(self, path, draft):
        if self.check_exits_work(path):
            with open(os.path.join(path, "ta", "work.json"), "r") as file:
                data = json.load(file)
                file.close()
            with open(os.path.join(path, "ta", "work.json"), "w") as file:
                data["workDraft"] = draft
                json.dump(data, file)
                file.close()
            print(" |-[*] draft has been written to work.json")

    def read_work(self, path) -> dict:
        if self.check_exits_work(path):
            with open(os.path.join(path, "ta", "work.json")) as file:
                data = json.load(file)
                file.close()
            return data
        else:
            return {}

    def read_filework(self, path):
        with open(os.path.join(path, 'ta', 'work.json')) as r:
            return json.load(r)
    
    def check_work_draft(self,path,draft):
        workDraft = self.read_filework(path)
        if draft == workDraft["workDraft"]:
            return False
        else:
            os.remove(os.path.join(path,"ta","work.json"))
            return True
            

            
            
