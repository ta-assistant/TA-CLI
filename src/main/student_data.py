import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from lib.file_management.work_editor import WorkEditor
from lib.file_management.file_management_lib import FileEditor, DirManagement



class StudentData:
    def __init__(self,path,filename) -> None:
        self.path = path
        self.draft = self.read_draft()
        self.pre_data = self.prepare_data(filename)
        self.pre_data = self.add_pre_student_data(self.setup_empty_data(),self.pre_data)

    def prepare_data(self,filename) -> dict:
        
        key=[]
        remainder = ""
        prework = {}
        for i in self.draft:
            if i == "{":
                remainder = ""
            elif i == "}":
                key.append(remainder)
            else:
                remainder += i
        list_filename = filename.split("_")
        for key,value in zip(key,list_filename):
            prework[key] = value

        return prework

    def read_draft(self):
        zdraft = WorkEditor("").read_file(self.path+r"\ta\draft.json")
        zdraft = zdraft["zip_file_draft"]
        return zdraft

    def read_work(self) -> dict:
        draft = WorkEditor("").read_file(self.path+r"\ta\draft.json")
        jdraft = draft["output_draft"]
        return jdraft

    def setup_empty_data(self) -> dict:
        empty_student = {}
        for i in self.read_work():
            empty_student[i] = "N/A"
        return empty_student

    def add_pre_student_data(self,empty_student,pre_student_data) -> dict:
        for i in pre_student_data:
            empty_student[i] = pre_student_data[i]
        return empty_student

    def data_input(self,post_student_data):
        for i in post_student_data:
            if post_student_data[i] == "N/A":
                data_input = input(f"Enter {i}: ")
                if data_input == "-99":
                    continue
                post_student_data[i] = data_input
        return post_student_data

    def ask(self) -> data_input:
        print("===========================")
        post_student_data = self.pre_data
        for i in post_student_data:
            if post_student_data[i] != "N/A":
                print(f"{i}: {post_student_data[i]}")
        print("===========================")
        return self.data_input(post_student_data)

if __name__ == "__main__":
    a = StudentData(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1")
    print(a.ask())
    # print(prepare_data(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1"))