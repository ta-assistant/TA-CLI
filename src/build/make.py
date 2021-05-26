import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)
import json
from lib.file_management.file_management_lib import DirManagement, FileEditor, WorkEditor
from lib.function_network.func_network import CallApi
def create_draft() -> bool:
    for i in range(8):
        draft_init = input("Do you want to fetch draft.json from the server:(yes,no) ")
        if draft_init.lower() == "yes":
            return True
        elif draft_init.lower() == "no":
            return False

def init_work_directory(path) -> bool:
    print(f"{path} makeing work directory")
    ta_path = os.path.join(path,"ta")
    if os.path.exists(ta_path):
        print(path+" is already a work directory")
    else:
        DirManagement().create_dir(ta_path)
    data = "prefix = https://ta-api.sirateek.dev/"
    with open(os.path.join(ta_path, "config.txt"), "w") as create:
        create.write(data)
        print("config.txt has been init.")
        create.close()
    print(f"{path} is ready")
    return create_draft()

def reset(path):
    ta_path = os.path.join(path,"ta")
    DirManagement.remove_dir(ta_path)