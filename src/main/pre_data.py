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


def check_filename_draft(filename: list,draft: list) -> bool:
    if len(filename) != len(draft):
        return False
    else:
        return True


def get_file_name(path,filename) -> dict:
    zdraft = JobEditor("").read_file(path+r"\ta\draft.json")
    zdraft = zdraft["zip_file_draft"]
    key=[]
    reminder = ""
    prejob = {}
    for i in zdraft:
        if i == "{":
            reminder = ""
        elif i == "}":
            key.append(reminder)
        else:
            reminder += i
    list_filename = filename.split("_")
    if not check_filename_draft(list_filename,key):
        print("Invalid file name " + filename)
        return {}
    for key,value in zip(key,list_filename):
        prejob[key] = value

    return prejob

if __name__ == "__main__":
    print(get_file_name(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1"))