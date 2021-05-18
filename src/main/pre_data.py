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

def prepare_data(path,filename) -> dict:
    zdraft = JobEditor("").read_file(path+r"\ta\draft.json")
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

if __name__ == "__main__":
    print(prepare_data(r"C:\Users\Admin\Desktop\ex1",r"6310546066_vitvara_ex1"))