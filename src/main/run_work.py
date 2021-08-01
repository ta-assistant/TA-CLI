from lib.cli_displayed.display_cli import display_api_status_message
import os
import json

from src.main.pre_work import Work
from src.main.student_data import StudentData

from lib.file_management import *
from lib.function_network import CallApi
from lib.cli_displayed import display_status_symbol, display_configuration


# private

def _check_config(path):
    return os.path.exists(os.path.join(path, "ta", "config.json"))


def _check_draft(path,draft_config):
    # Not have draft.json
    if not os.path.exists(os.path.join(path, "ta", "draft.json")):
        # Have an api-key
        if exsitapikey():
            return draft_config
        # Not have an api-key and draft.json
        return False
    # Have an draft.json
    else:
        return True


def _check_state(config_state, draft_state):
    if config_state and draft_state:
        # Have config.json and draft.json
        return True
    else:
        # Display Error message
        display_status_symbol(1, 2, "Error!!")
        if config_state:
            # Have config.json
            display_status_symbol(2, 0, "config.json")
        else:
            # Not have config.json
            display_status_symbol(2, 1, "config.json not found")
        if draft_state:
            # Have draft.json
            display_status_symbol(2, 0, "draft.json")
        else:
            # Not have draft.json
            display_status_symbol(2, 1, "draft.json not found")
        display_status_symbol(0, 1, "Failed")
        return False


def _preparework(path,draft_config):
    config_state = _check_config(path)
    draft_state = _check_draft(path,draft_config)

    # Check that config.json is exists or not 
    display_status_symbol(1,0 if config_state else 1,"Checking config.json")
    # Check that draft.json is exists or not
    display_status_symbol(1,0 if draft_state else 1,"Checking draft.json")
    return _check_state(config_state, draft_state)


def _draft_config():
    # Ask user that they want to read draft.json or fetch draft from the server
    print("Do you want to use draft from draft.json or fetch from the server")
    while True:
        user_in = input("(R)ead from file or (F)etch from server: ")
        # Check user input
        if user_in.lower() in "RrFf":
            break
    # if user input = r return False
    # if user input = f return True
    return user_in.lower() == "f"


def _display_draft(draft):
    # Init outputdraft and filedraft
    outputdraft = draft["outputDraft"]
    filedraft = draft["fileDraft"]
    # Display drafts item
    display_status_symbol(2,2,f"fileDraft: {filedraft}")
    display_status_symbol(2,2,f"outputDraft: {outputdraft}",True)

def _get_draft(path,draft_config):
    if draft_config:
        # Init CallAPi obj
        API = CallApi(path)
        # Fetch draft
        # draft can be False and json obj
        draft = API.fetch()
        # Display API message
        display_status_symbol(1,2,"Fetching draft ...")
        display_api_status_message(API.api_massage(),2,True)
        if not draft:
            return None, False
        # Display draft's item
        display_status_symbol(1,2,"Choosen draft")
        _display_draft(draft)
    else:
        # Read draft.json
        with open(os.path.join(path, "ta", "draft.json"), "r") as draftfile:
            draft = json.load(draftfile)
            draftfile.close()
        # Display draft's item
        display_status_symbol(1,2,"Choosen draft")
        _display_draft(draft)
    return draft, True


def _add_data_to_work(path, draft, workId):
    # Init Work obj
    work = Work()
    # Add element to Work obj
    work.draft = draft
    work.path = path
    work.workId = workId
    # Check Work items (draf workid ta_path)
    if work.property_is_ready():
        work_path = os.path.join(path, "ta", "work.json")
        # Create work.json
        if work.create():
            display_status_symbol(1, 0, f"{work_path} created")
        else:
            # work.json is already created
            display_status_symbol(1, 2, f"{work_path} already exists")
    else:
        # Work's item is not ready
        display_status_symbol(1, 1, f"Error: Invalid component")
        component = {"draft":work.draft,"path":work.path,"workId":work.workId}
        component_size = len({"draft":work.draft,"path":work.path,"workId":work.workId})
        for index,item in enumerate(component.items()):
            # Display missing item
            display_status_symbol(2,1 if item[1] == None else 0, f"{item[0]}",component_size == index+1)
        return False, None
    return True, work


def _manage_work(path, draft):
    # Call menage_work_file
    if not manage_work_file(path, draft):
        return False
    display_status_symbol(0, 0,"Finish")
    return True


def _student_checking(path, work, file, openvs, onebyone):
    # Init StudentData obj
    student = StudentData(path=work.path, filename=file, draft=work.draft)
    # Read work.json scores
    with open(os.path.join(path, "ta", "work.json"), "r") as workfile:
        scores = json.load(workfile)["scores"]
        workfile.close
    # Prepare student data
    student.prepare_student_data()
    _did_student_checked(path,work, file, student, scores, openvs, onebyone)


def _did_student_checked(path,work, file, student, scores, openvs, onebyone):
    # Check that that student is already scored or not
    if student.check_work_score(scores):
        # open vscode 1 by 1 file
        if openvs and onebyone:
            assignmentpath = os.path.join(path,"ta", "Assignment", file)
            print(assignmentpath)
            os.system(f"code \"{assignmentpath}\"")
        work.write_work(student.ask())


def _scoring(path, work, openvs, onebyone):
    # Init Assignment path
    list_file = os.listdir(os.path.join(path, "ta", "Assignment"))
    assignmentpath = os.path.join("ta", "Assignment")
    # open vscode path=Aassignment directory
    if openvs and not onebyone:
        os.system(f"code \"{assignmentpath}\"")
    # Ignore ta directory
    for file in list_file:
        if "." in file or file == "ta":
            continue
        # Checking student work.
        _student_checking(path, work, file, openvs, onebyone)

# public

def run_work(path, openvs=True, onebyone=False):
    # Fetch or read draft
    draft_config = _draft_config()
    if draft_config and not exsitapikey():
        display_status_symbol(0,1,"You don't have an api-key please login and try again.")
        return False
    display_status_symbol(0,2,"starting...")

    # Checking draft and config.json that are exist or not
    # ! If draft.json not exists but user choose to fetch draft from server it won't get error
    if not _preparework(path,draft_config):
        return False

    # Get component
    draft, draft_state = _get_draft(path,draft_config)
    if not draft_state:
        display_status_symbol(0,1,"Failed can not fetch draft")
        return False
    config = readconfig(path)
    workId = config["workId"]
    ta_api = config["prefix"]

    # Check component then write data to work.json
    workstate, work = _add_data_to_work(path, draft, workId)
    if not workstate:
        # Component is not ready
        display_status_symbol(0,1,"Failed Invalid conponent")
        return False

    # Move Extract file to Assignment dir.
    if not _manage_work(path, draft):
        # None of them are follow the draft
        display_status_symbol(1, 1,"All file aren't follow the draft")
        display_status_symbol(0,1,"Failed")
        return False

    # Number of file in Assignment directory
    num_file = len(os.listdir(os.path.join(path, "ta", "Assignment")))

    display_configuration(draft,workId,ta_api,num_file)
    print("If you want to stop the process press Ctrl^C\n")

    # Scoring part
    _scoring(path, work, openvs, onebyone)
    return True