import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))

os.chdir(parentdir+r"\lib\file_management")
sys.path.insert(0,os.getcwd())

from job_editor import JobEditor

def check_draft(path: str) -> bool:
    if os.path.exists(path+r"\ta\draft.json"):
        draft = JobEditor("").read_file(path+r"\ta\draft.json")
        return True
    else:
        return False


if __name__ == "__main__":
    check_draft(r"C:\Users\Admin\Desktop\ex1")
