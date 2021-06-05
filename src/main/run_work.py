import os, json
from src.main.pre_work import Work
from lib.file_management.extract import unzipfile
from src.main.student_data import StudentData
from lib.file_management.configeditor import ConfigEditor
def run_work(path):
    if not os.path.exists(os.path.join(path,"ta","draft.json")):
        print("draft.json not exists.")
        return False
    if not os.path.exists(os.path.join(path,"ta","config.json")):
        print("config.json not exists.")
        return False
    with open(os.path.join(path,"ta","draft.json"),"r") as draftfile:
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

    unzipfile(path)
    list_file = os.listdir(path)
    os.system(f"code {path}")
    for file in list_file:
        if "." in file or file == "ta":
            continue
        student = StudentData(
            path=work.path, filename=file, draft=work.draft)
        with open(os.path.join(path,"ta","work.json"),"r") as workfile:
            scores = json.dump(workfile)["scores"]
            workfile.close
        student.prepare_student_data()
        if student.check_work_score(scores):
            work.write_work(student.ask())
    return True