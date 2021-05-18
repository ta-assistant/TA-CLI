import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor

def check_empty_data(path,pre_student_dict):
    zdraft = JobEditor("").read_file(path+r"\ta\draft.json")
    zdraft = zdraft["output_draft"]




def ask(path):
    while True:
        pass

if __name__ == "__main__":
    check_empty_data(r"C:\Users\Admin\Desktop\ex1"+)