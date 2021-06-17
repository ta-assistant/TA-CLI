from lib.function_network.func_network import CallApi
from lib.file_management.configeditor import ConfigEditor
from lib.file_management.file_management_lib import DirManagement
from lib.file_management.createapikeyfile import SaveApiKey
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir)


def init_work_directory(path, workid) -> bool:
    print(f"{path} makeing work directory")
    ta_path = os.path.join(path, "ta")
    config_path = os.path.join(path, "ta", "config.json")
    draft_path = os.path.join(path, "ta", "draft.json")
    if os.path.exists(ta_path):
        print(path+" is already a work directory")
    else:
        DirManagement().create_dir(ta_path)
    if os.path.exists(config_path):
        print("config.json already exists.")
    else:
        ConfigEditor(workid, path).writeconfig()
    if os.path.exists(draft_path):
        print("draft.json already exists.")
    elif not SaveApiKey().exsitapikey():
        print("## API-key not exists ##")
    else:
        CallApi(path)
    if os.path.exists(draft_path) and os.path.exists(config_path) and os.path.exists(ta_path):
        print(f"{path} is ready")
    else:
        print("Something is missing please try again.")
        print(
            f"draft.json: {os.path.exists(draft_path)}\nconfig.json: {os.path.exists(config_path)}\nta directory: {os.path.exists(ta_path)}")


def reset(path):
    ta_path = os.path.join(path, "ta")
    DirManagement.remove_dir(ta_path)
