import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor
from file_management_lib import DirManagement, FileEditor


def init_work_directory(path) -> bool:
    print(f"{path} makeing work directory")
    if os.path.exists(path+r"\ta"):
        print(path+" is already a work directory")
    else:
        DirManagement().create_dir(path+r"\ta")
    print("Now you can add your draft.json")
    for i in range(8):
        draft_init = input("Do you want to fetch draft.json from the server:(yes,no) ")
        if draft_init.lower() == "yes":
            break
        elif draft_init.lower() == "no":
            break
    # extract function
    print(f"{path} is ready")

if __name__ == "__main__":
    init_work_directory(r"C:\Users\Admin\Desktop\ex1")
    



