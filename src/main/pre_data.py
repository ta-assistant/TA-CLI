import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor

def get_file_name(path,filename):
    zdraft = JobEditor("").read_file(path+r"\ta\draft.json")
    print(zdraft["zip_file_draft"])

get_file_name(r"C:\Users\Admin\Desktop\ex1","Asdfasdfsa")