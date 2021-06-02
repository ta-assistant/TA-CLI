import os, json
from src.main.pre_work import Work
from lib.file_management.extract import unzipfile
from src.main.student_data import StudentData

def run_work(path,workID,draft):
    work = Work()
    work.draft = draft
    work.path = path
    work.workId = workID
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