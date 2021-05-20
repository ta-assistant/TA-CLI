import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir)
sys.path.insert(0,os.getcwd())

from lib.file_management.file_management_lib import FileEditor, DirManagement,WorkEditor

def inask(question):
    answer = input(question)
    return answer
class StudentData:
    def __init__(self,path,filename) -> None:
        self.path = path
        self.draft_path = os.path.join(path,"ta","draft.json")
        self.draft_zip = self.read_draft_zip()
        self.draft_work = self.read_draft_work()
        self.pre_data = None
        self.filename = filename

    def prepare_data(self) -> dict:
        key=[]
        remainder = ""
        prework = {}
        for i in self.draft_zip:
            if i == "{":
                remainder = ""
            elif i == "}":
                key.append(remainder)
            else:
                remainder += i
        list_filename = self.filename.split("_")
        for key,value in zip(key,list_filename):
            prework[key] = value

        self.pre_data = prework

    def read_draft_zip(self):
        if os.path.exists(self.draft_path):
            zdraft = WorkEditor("").read_file(self.draft_path)
            zdraft = zdraft["zip_file_draft"]
            return zdraft
        return None

    def read_draft_work(self) -> dict:
        if os.path.exists(self.draft_path):
            draft = WorkEditor("").read_file(self.draft_path)
            jdraft = draft["output_draft"]
            return jdraft
        return None

    def setup_empty_data(self) -> dict:
        empty_student = {}
        for i in self.draft_work:
            empty_student[i] = "N/A"
        return empty_student

    def add_pre_student_data(self,empty_student) -> dict:
        for i in self.pre_data:
            empty_student[i] = self.pre_data[i]
        self.pre_data = empty_student
    
    def data_input(self,post_student_data):
        for i in post_student_data:
            if post_student_data[i] == "N/A":
                data_input = inask(f"Enter {i}: ")
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
        post_data = self.data_input(post_student_data)
        return post_data

if __name__ == "__main__":
    stu1 = StudentData(r"C:\Users\Admin\Desktop\ex1","6310546066_vitvara_ex1")
    stu1.prepare_data()
    stu1.add_pre_student_data(stu1.setup_empty_data())
    print(stu1.ask())
    