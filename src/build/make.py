from lib.file_management.create_apikeyfile import readapikey
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

def _display_check_api_key_status(path,key_state):
    # Check apikey path
    if key_state:
        display_status_symbol(1,0,"Checking API-KEY")
    else:
        # Send apikey not found message
        display_status_symbol(1,1,"Checking API-KEY")
        display_status_symbol(2,1,"API-KEY not found",end=True)

def _display_call_api(path):
    # Init callapi obj
    callapi_obj = CallApi(path)
    # Fetch draft it will create draft.json in ta dir
    apistate = _fetch_draft(callapi_obj)
    # Send message
    display_status_symbol(1,2,"Fetching draft ...")
    display_api_status_message(_fetch_api_massage(callapi_obj),2,end=True)

# public
def init_work_directory(path, workId) -> bool:
    # Init file path
    config_path = os.path.join(path, "ta", "config.json")
    ta_path = os.path.join(path, "ta")
    draft_path = os.path.join(path, "ta", "draft.json")
    # Check api-key
    keystate = _check_api_key(path)
    # Start
    print(f"[*] {path} makeing work directory")
    # Create ta directory
    _display_create_ta_dir_status(path)
    # Check config if it not exists create config.json
    # If workid is change config.json will change to new workid
    _display_check_config_status(workId, path)
    # Display api-key status
    _display_check_api_key_status(path,keystate)
    # Have an apikey
    if keystate:
        # Call Api (Fetch draft) and write draft.json
        _display_call_api(path)
    # Check all items [ draft.json, config.json, and ta directory ]
    if os.path.exists(draft_path) and os.path.exists(config_path) and os.path.exists(ta_path):
        display_status_symbol(0,0,f"{path} is ready")
        return True
    else:
        # Some items is not exist.
        display_status_symbol(0,1,"Something went wrong please try again.")
        return False

def reset(path):
    ta_path = os.path.join(path, "ta")
    DirManagement.remove_dir(ta_path)