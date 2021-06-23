import os
import json
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


def check_state(config_state,draft_state,path):
    if config_state and draft_state:
        return True
    else:
        display_typo(1,(config_state and draft_state),"Property is not ready please try again",
                    optional_massage=f"CONFIG : {config_state} / DRAFT : {draft_state} / API-KEY : {SaveApiKey().exsitapikey()}")
        print("[*]")
        return False
    

def run_work(path, openvs=True, onebyone=False):
    print("[*] starting...")
    config_state = check_config(path)
    draft_state = check_draft(path)
    display_typo(1,config_state,"checking config.json")
    display_typo(1,draft_state,"checking draft.json")
    if not check_state(config_state, draft_state, path):
        return False
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
    work = Work()
    work.draft = draft
    work.path = path
    work.workId = ConfigEditor(path=path).readconfig()
    if work.property_is_ready():
        work.create()
    else:
        print("property is not ready")
        print(work.draft)
        print(work.path)
        print(work.workId)
        return False

    if not unzipfile(path,draft["fileDraft"]):
        print("[*] all file aren't follow the draft")
        return False
    print("[/] finish")

    list_file = os.listdir(os.path.join(path, "ta", "extract"))
    extractpath = os.path.join("ta", "extract")
    if openvs and not onebyone:
        os.system(f"code {extractpath}")
    for file in list_file:
        if "." in file or file == "ta":
            continue
        student = StudentData(
            path=work.path, filename=file, draft=work.draft)
        with open(os.path.join(path, "ta", "work.json"), "r") as workfile:
            scores = json.load(workfile)["scores"]
            workfile.close
        student.prepare_student_data()
        if student.check_work_score(scores):
            if openvs and onebyone:
                extractpath = os.path.join("ta", "extract", file)
                os.system(f"code {extractpath}")
            work.write_work(student.ask())
    return True
