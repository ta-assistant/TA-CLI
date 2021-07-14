import os
import json
# import pandas as pd
from datetime import datetime
from src.main.pre_work import Work
from lib.file_management.extract import unzipfile
from src.main.student_data import StudentData
from lib.file_management.configeditor import ConfigEditor
from lib.function_network.func_network import CallApi
from lib.file_management.createapikeyfile import SaveApiKey
from lib.cli_displayed.dis_cli import display_typo


def check_config(path):
    if not os.path.exists(os.path.join(path, "ta", "config.json")):
        return False
    else:
        return True


def check_draft(path):
    if not os.path.exists(os.path.join(path, "ta", "draft.json")) and not SaveApiKey().exsitapikey():
        return False
    else:
        return True


def check_state(config_state, draft_state, path):
    if config_state and draft_state:
        return True
    else:
        display_typo(1, (config_state and draft_state), "Property is not ready please try again",
                     optional_massage=f"CONFIG : {config_state} / DRAFT : {draft_state} / API-KEY : {SaveApiKey().exsitapikey()}")
        print("[*]")
        return False


def preparework(path):
    config_state = check_config(path)
    draft_state = check_draft(path)
    display_typo(1, config_state, "checking config.json")
    display_typo(1, draft_state, "checking draft.json")

    if not check_state(config_state, draft_state, path):
        return False
    return True


def draft_config(path):
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


def add_data_to_work(path, draft):
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


def unzip_homework(path, draft):
    if not unzipfile(path, draft["fileDraft"]):
        print("[*] all file aren't follow the draft")
        return False
    print("[/] finish")
    return True


def student_checking(path, work, file, openvs, onebyone):
    student = StudentData(path=work.path, filename=file, draft=work.draft)
    with open(os.path.join(path, "ta", "work.json"), "r") as workfile:
        scores = json.load(workfile)["scores"]
        workfile.close
    student.prepare_student_data()
    did_student_checked(path,work, file, student, scores, openvs, onebyone)


def did_student_checked(path,work, file, student, scores, openvs, onebyone):
    if student.check_work_score(scores):
        if openvs and onebyone:
            assignmentpath = os.path.join(path,"ta", "Assignment", file)
            print(assignmentpath)
            os.system(f"code {assignmentpath}")
        work.write_work(student.ask())


def scoring(path, work, openvs, onebyone):
    list_file = os.listdir(os.path.join(path, "ta", "Assignment"))
    assignmentpath = os.path.join("ta", "Assignment")
    if openvs and not onebyone:
        os.system(f"code {assignmentpath}")
    for file in list_file:
        if "." in file or file == "ta":
            continue
        student_checking(path, work, file, openvs, onebyone)


def run_work(path, openvs=True, onebyone=False):
    print("[*] starting...")
    if not preparework(path):
        return False
    draft = draft_config(path)
    workstate, work = add_data_to_work(path, draft)
    if not workstate:
        return False
    if not unzip_homework(path, draft):
        return False
    scoring(path, work, openvs, onebyone)
    return True
