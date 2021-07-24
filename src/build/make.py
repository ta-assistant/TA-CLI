import os
import sys
import inspect

from lib.cli_displayed import display_typo
from lib.file_management import  ConfigEditor, DirManagement
from lib.function_network import CallApi, SaveApiKey


# private
def _create_ta_dir(path):
    ta_path = os.path.join(path, "ta")
    if os.path.exists(ta_path):
        return False
    else:
        DirManagement().create_dir(ta_path,out=False)
        return True


def _check_config(workid, path):
    config_path = os.path.join(path, "ta", "config.json")
    if os.path.exists(config_path):
        return False
    else:
        ConfigEditor(workid, path).writeconfig()
        return True


def _check_api_key(path):
    if SaveApiKey().exsitapikey():
        return True
    else:
        return False



def _fetch_draft(callapi_func):
    return callapi_func.createworkdraft()
 


def _fetch_api_massage(apiobj):
    return apiobj.api_massage()


# public
def init_work_directory(path, workid) -> bool:
    config_path = os.path.join(path, "ta", "config.json")
    ta_path = os.path.join(path, "ta")
    draft_path = os.path.join(path, "ta", "draft.json")

    keystate = _check_api_key(path)

    print(f"[*] {path} makeing work directory")
    display_typo(1,_create_ta_dir(path),f"Creating workDirectory {path}",
                optional_massage="Skipped. Already exists",when=False)
    display_typo(1,_check_config(workid, path),"Creating `config.json`",
                optional_massage="Skipped. Already exists",when=False)
    display_typo(1,keystate,"Checking API-KEY",
                optional_massage="API-KEY doesn't exists",when=False)

    if keystate:
        callapi_obj = CallApi(path)
        apistate = _fetch_draft(callapi_obj)
        display_typo(1,apistate,"fetching draft.json ...")
        display_typo(2,apistate,_fetch_api_massage(callapi_obj))
    print(" |")
    
    if os.path.exists(draft_path) and os.path.exists(config_path) and os.path.exists(ta_path):
        print(f"[/] {path} is ready")
        return True
    else:
        print("[x] Something is missing please try again.\n")
        print(
            f"draft.json: {os.path.exists(draft_path)}\nconfig.json: {os.path.exists(config_path)}\nta directory: {os.path.exists(ta_path)}")
        return False

def reset(path):
    ta_path = os.path.join(path, "ta")
    DirManagement.remove_dir(ta_path)