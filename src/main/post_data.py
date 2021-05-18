import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor

def read_job(path):
    draft = JobEditor("").read_file(path+r"\ta\draft.json")
    jdraft = draft["output_draft"]
    return jdraft

def setup_empty_data(path):
    empty_student = {}
    for i in read_job(path):
        empty_student[i] = "N/A"
    return empty_student

def add_pre_student_data(empty_student,pre_student_data):
    for i in pre_student_data:
        empty_student[i] = pre_student_data[i]
    return empty_student
    

def ask(post_student_data):
    print("===========================")
    for i in post_student_data:
        if post_student_data[i] != "N/A":
            print(f"{i}: {post_student_data[i]}")
    print("===========================")
    for i in post_student_data:
        if post_student_data[i] == "N/A":
            data_input = input(f"Enter {i}: ")
            post_student_data[i] = data_input
    return post_student_data

    
if __name__ == "__main__":
    pre_student = {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1'}
    empty_student = setup_empty_data(r"C:\Users\Admin\Desktop\ex1")
    a = add_pre_student_data(empty_student,pre_student)
    print(a)
    print(ask(a))
    