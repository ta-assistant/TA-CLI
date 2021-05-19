import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor


class StudentData:
    def __init__(self,path,filename) -> None:
        self.path = path
        self.pre_data = self.prepare_data(filename)
        self.pre_data = self.add_pre_student_data(self.setup_empty_data(),self.pre_data)

    def check_draft(self) -> bool:
        if os.path.exists(self.path+r"\ta\draft.json"):
            draft = JobEditor("").read_file(self.path+r"\ta\draft.json")
            return True
        else:
            return False

    def prepare_data(self,filename) -> dict:
        zdraft = JobEditor("").read_file(self.path+r"\ta\draft.json")
        zdraft = zdraft["zip_file_draft"]
        key=[]
        remainder = ""
        prejob = {}
        for i in zdraft:
            if i == "{":
                remainder = ""
            elif i == "}":
                key.append(remainder)
            else:
                remainder += i
        list_filename = filename.split("_")
        for key,value in zip(key,list_filename):
            prejob[key] = value

        return prejob


    def read_job(self) -> dict:
        draft = JobEditor("").read_file(self.path+r"\ta\draft.json")
        jdraft = draft["output_draft"]
        return jdraft

    def setup_empty_data(self) -> dict:
        empty_student = {}
        for i in self.read_job():
            empty_student[i] = "N/A"
        return empty_student

    def add_pre_student_data(self,empty_student,pre_student_data) -> dict:
        for i in pre_student_data:
            empty_student[i] = pre_student_data[i]
        return empty_student

    def ask(self) -> bool:
        print("===========================")
        post_student_data = self.pre_data
        for i in post_student_data:
            if post_student_data[i] != "N/A":
                print(f"{i}: {post_student_data[i]}")
        print("===========================")
        for i in post_student_data:
            if post_student_data[i] == "N/A":
                data_input = input(f"Enter {i}: ")
                if data_input == "-99":
                    return False
                post_student_data[i] = data_input
        return True

if __name__ == "__main__":
    a = StudentData(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1")
    print(a.ask())
    # print(prepare_data(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1"))