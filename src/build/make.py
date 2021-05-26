import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)
<<<<<<< HEAD

from lib.file_management.file_management_lib import DirManagement, FileEditor, WorkEditor

=======
import json
from lib.file_management.file_management_lib import DirManagement, FileEditor, WorkEditor
from lib.function_network.func_network import CallApi
>>>>>>> master
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
<<<<<<< HEAD
        return False
    else:
        DirManagement().create_dir(ta_path)
    print("Now you can add your draft.json")
    if create_draft():
        pass
    print(f"{path} is ready")
    return True

def reset(path):
    ta_path = os.path.join(path,"ta")
    DirManagement.remove_dir(ta_path)
    
if __name__ == "__main__":
    init_work_directory(r"C:\Users\Admin\Desktop\ex1")
    



=======
    else:
        DirManagement().create_dir(ta_path)
    data = 'prefix = '
    with open(os.path.join(ta_path, "config.txt"), "w") as create:
        json.dump(data, create)
        print("config.txt has been init.")
        create.close()
    print(f"{path} is ready")
    return create_draft()

def reset(path):
    ta_path = os.path.join(path,"ta")
    DirManagement.remove_dir(ta_path)
>>>>>>> master
