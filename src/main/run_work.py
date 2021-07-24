import os
import json
from datetime import datetime

from src.main.pre_work import Work
from src.main.student_data import StudentData

from lib.file_management import manage_work_file, ConfigEditor, SaveApiKey
from lib.function_network import CallApi
from lib.cli_displayed import display_typo


# private

def _check_config(path):
    if not os.path.exists(os.path.join(path, "ta", "config.json")):
        return False
    else:
        return True


def _check_draft(path):
    if not os.path.exists(os.path.join(path, "ta", "draft.json")) and not SaveApiKey().exsitapikey():
        return False
    else:
        return True


def _check_state(config_state, draft_state, path):
    if config_state and draft_state:
        return True
    else:
        display_typo(1, (config_state and draft_state), "Property is not ready please try again",
                     optional_massage=f"CONFIG : {config_state} / DRAFT : {draft_state} / API-KEY : {SaveApiKey().exsitapikey()}")
        print("[*]")
        return False


def _preparework(path):
    config_state = _check_config(path)
    draft_state = _check_draft(path)
    display_typo(1, config_state, "checking config.json")
    display_typo(1, draft_state, "checking draft.json")

    if not _check_state(config_state, draft_state, path):
        return False
    return True


def _draft_config(path):
    print("Do you want to use draft from draft.json or fetch from the server")
    while True:
        user_in = input("(R)ead from file or (F)etch from server: ")
        if user_in.lower() in "RrFf":
            break
    if user_in.lower() == "f":
        draft = CallApi(path).fetch()
        print(draft)
    else:
        with open(os.path.join(path, "ta", "draft.json"), "r") as draftfile:
            draft = json.load(draftfile)
            draftfile.close()
    return draft


def _add_data_to_work(path, draft):
    work = Work()
    work.draft = draft
    work.path = path
    work.workId = ConfigEditor(path=path).readconfig()["workId"]
    if work.property_is_ready():
        work_path = os.path.join(path, "ta", "work.json")
        if work.create():
            print(f" |-[/] {work_path} created")
        else:
            print(f" |-[X] {work_path} already exists")
    else:
        print("property is not ready")
        print(work.draft)
        print(work.path) 
        print(work.workId)
        return False, None
    return True, work


def _manage_work(path, draft):
    if not manage_work_file(path, draft["fileDraft"]):
        print("[*] all file aren't follow the draft")
        return False
    print("[/] finish")
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
    print("[*] starting...")
    if not _preparework(path):
        return False
    draft = _draft_config(path)
    workstate, work = _add_data_to_work(path, draft)
    if not workstate:
        return False
    if not _manage_work(path, draft):
        return False
    _scoring(path, work, openvs, onebyone)
    return True