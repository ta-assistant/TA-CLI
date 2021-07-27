import os
import json

from src.main.pre_work import Work
from src.main.student_data import StudentData

from lib.file_management import manage_work_file, ConfigEditor, SaveApiKey
from lib.function_network import CallApi
from lib.cli_displayed import display_status_symbol, display_configuration


# private

def _check_config(path):
    if not os.path.exists(os.path.join(path, "ta", "config.json")):
        return False
    else:
        return True


def _check_draft(path,draft_config):
    if SaveApiKey().exsitapikey() and not os.path.exists(os.path.join(path, "ta", "draft.json")) and not draft_config:
        return False
    elif not SaveApiKey().exsitapikey() and not os.path.exists(os.path.join(path, "ta", "draft.json")):
        return False
    else:
        return True


def _check_state(config_state, draft_state):
    if config_state and draft_state:
        return True
    else:
        display_status_symbol(1, 2, "Error!!")
        if config_state:
            display_status_symbol(2, 0, "config.json")
        else:
            display_status_symbol(2, 1, "config.json not found")
        if draft_state:
            display_status_symbol(2, 0, "draft.json")
        else:
            display_status_symbol(2, 1, "draft.json not found")
        
        display_status_symbol(0, 2, "")
        return False


def _preparework(path,draft_config):
    config_state = _check_config(path)
    draft_state = _check_draft(path,draft_config)

    # Check that config.json is exists or not
    
    if config_state:
        display_status_symbol(1,0,"Checking config.json")
    else:
        display_status_symbol(1,1,"Checking config.json")

    # Check that draft.json is exists or not
    
    if draft_state:
        display_status_symbol(1,0,"Checking draft.json")
    else:
        display_status_symbol(1,1,"Checking draft.json")

    if not _check_state(config_state, draft_state):
        return False
    return True


def _draft_config(path):
    print("Do you want to use draft from draft.json or fetch from the server")
    while True:
        user_in = input("(R)ead from file or (F)etch from server: ")
        if user_in.lower() in "RrFf":
            break
    if user_in.lower() == "f":
        return True
    else:
        return False

def _display_draft(draft):
    outputdraft = draft["outputDraft"]
    filedraft = draft["fileDraft"]
    display_status_symbol(2,2,f"fileDraft: {filedraft}")
    display_status_symbol(2,2,f"outputDraft: {outputdraft}",True)

def _get_draft(path,draft_config):
    if draft_config:
        draft = CallApi(path).fetch()
        display_status_symbol(1,2,"Choosen draft")
        _display_draft(draft)
    else:
        with open(os.path.join(path, "ta", "draft.json"), "r") as draftfile:
            draft = json.load(draftfile)
            draftfile.close()
        display_status_symbol(1,2,"Choosen draft")
        _display_draft(draft)
        
    return draft


def _add_data_to_work(path, draft, workId):
    work = Work()
    work.draft = draft
    work.path = path
    work.workId = workId
    if work.property_is_ready():
        work_path = os.path.join(path, "ta", "work.json")
        if work.create():
            display_status_symbol(1, 0, f"{work_path} created")
        else:
            display_status_symbol(1, 2, f"{work_path} already exists")
    else:
        display_status_symbol(1, 1, f"Error: Invalid component")
        component = {"draft":work.draft,"path":work.path,"workId":work.workId}
        count = 0
        end = False
        for k,i in component.items():
            count += 1
            if count == len(component):
                end = True
            if i == None:
                display_status_symbol(2, 1, f"{k}",end)
            else:
                display_status_symbol(2, 0, f"{k}",end)
        
        return False, None
    return True, work


def _manage_work(path, draft):
    if not manage_work_file(path, draft):
        display_status_symbol(1, 1,"all file aren't follow the draft")
        return False
    display_status_symbol(0, 0,"Finish")
    return True


def _student_checking(path, work, file, openvs, onebyone):
    student = StudentData(path=work.path, filename=file, draft=work.draft)
    with open(os.path.join(path, "ta", "work.json"), "r") as workfile:
        scores = json.load(workfile)["scores"]
        workfile.close
    student.prepare_student_data()
    _did_student_checked(path,work, file, student, scores, openvs, onebyone)


def _did_student_checked(path,work, file, student, scores, openvs, onebyone):
    if student.check_work_score(scores):
        if openvs and onebyone:
            assignmentpath = os.path.join(path,"ta", "Assignment", file)
            print(assignmentpath)
            os.system(f"code \"{assignmentpath}\"")
        work.write_work(student.ask())


def _scoring(path, work, openvs, onebyone):
    list_file = os.listdir(os.path.join(path, "ta", "Assignment"))
    assignmentpath = os.path.join("ta", "Assignment")
    if openvs and not onebyone:
        os.system(f"code \"{assignmentpath}\"")
    for file in list_file:
        if "." in file or file == "ta":
            continue
        _student_checking(path, work, file, openvs, onebyone)

# public

def run_work(path, openvs=True, onebyone=False):
    # Fetch or read draft
    draft_config = _draft_config(path)

    display_status_symbol(0,2,"starting...")

    # Checking draft and config.json that are exist or not
    # ! If draft.json not exists but user choose to fetch draft from server it won't get error
    if not _preparework(path,draft_config):
        return False

    # Get component
    draft = _get_draft(path,draft_config)
    config = ConfigEditor(path=path).readconfig()
    workId = config["workId"]
    ta_api = config["prefix"]

    # Check component then write data to work.json
    workstate, work = _add_data_to_work(path, draft, workId)
    if not workstate:
        # Component is not ready
        display_status_symbol(0,1,"Failed")
        return False

    # Move Extract file to Assignment dir.
    if not _manage_work(path, draft):
        # None of them are follow the draft
        display_status_symbol(0,1,"Failed")
        return False

    # Number of file in Assignment directory
    num_file = len(os.listdir(os.path.join(path, "ta", "Assignment")))

    display_configuration(draft,workId,ta_api,num_file)
    print("If you want to stop the process press Ctrl^C\n")

    # Scoring part
    _scoring(path, work, openvs, onebyone)
    return True