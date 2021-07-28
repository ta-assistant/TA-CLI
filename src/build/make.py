import os
import sys
import inspect

from lib.cli_displayed import display_status_symbol, display_api_status_message
from lib.file_management import writeconfig , readconfig, DirManagement
from lib.function_network import CallApi, exsitapikey


# private
def _create_ta_dir(path):
    ta_path = os.path.join(path, "ta")
    if os.path.exists(ta_path):
        return False
    else:
        DirManagement().create_dir(ta_path,out=False)
        return True


def _check_config(workId, path):
    config_path = os.path.join(path, "ta", "config.json")
    if os.path.exists(config_path):
        return False
    else:
        writeconfig(path,workId)
        return True


def _check_api_key(path):
    return exsitapikey()


def _fetch_draft(callapi_func):
    return callapi_func.createworkdraft()
 


def _fetch_api_massage(apiobj):
    return apiobj.api_massage()

def _display_create_ta_dir_status(path):
    
    if _create_ta_dir(path):
        display_status_symbol(1,0,f"Creating workDirectory {path}")
    else:
        display_status_symbol(1,2,f"Creating workDirectory {path}")
        display_status_symbol(2,2,f"Skipped. Already exists",end=True)

def _display_check_config_status(workId, path):
    if _check_config(workId, path):
        display_status_symbol(1,0,f"Creating `config.json`")
    else:
        # check that old_workid is the same with user input workid
        old_workId = readconfig(path)["workId"]
        if old_workId == workId:
            display_status_symbol(1,2,f"Creating `config.json`")
            display_status_symbol(2,2,f"Skipped. Already exists",end=True)
        
        else:
            # if it not the same with user input workid rewrite new workid to config.json
            writeconfig(path,workId)
            display_status_symbol(1,1,f"Creating `config.json`")
            display_status_symbol(2,2,f"workId has been changed to {workId}",end=True)

def _display_check_api_key_status(path):
    if _check_api_key(path):
        display_status_symbol(1,0,"Checking API-KEY")
    else:
        display_status_symbol(1,1,"Checking API-KEY")
        display_status_symbol(2,1,"API-KEY not found",end=True)

def _display_call_api(path):
    callapi_obj = CallApi(path)
    apistate = _fetch_draft(callapi_obj)
    display_status_symbol(1,2,"Fetching draft ...")
    display_api_status_message(_fetch_api_massage(callapi_obj),2,end=True)

# public
def init_work_directory(path, workId) -> bool:
    config_path = os.path.join(path, "ta", "config.json")
    ta_path = os.path.join(path, "ta")
    draft_path = os.path.join(path, "ta", "draft.json")

    keystate = _check_api_key(path)

    print(f"[*] {path} makeing work directory")
    _display_create_ta_dir_status(path)
    _display_check_config_status(workId, path)
    _display_check_api_key_status(path)
    if keystate:
        _display_call_api(path)
    
    if os.path.exists(draft_path) and os.path.exists(config_path) and os.path.exists(ta_path):
        display_status_symbol(0,0,f"{path} is ready")
        return True
    else:
        display_status_symbol(0,1,"Something went wrong please try again.")
        return False

def reset(path):
    ta_path = os.path.join(path, "ta")
    DirManagement.remove_dir(ta_path)