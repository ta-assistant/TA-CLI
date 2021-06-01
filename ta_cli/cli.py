import click
import os
import sys
import json

from click.decorators import command
from src.build import make
from src.main.draft_check import check_draft
from src.main.student_data import StudentData
from src.main.pre_work import Work
from lib.file_management.extract import unzipfile
from lib.function_network.func_network import CallApi, SendData
from lib.file_management.configeditor import ConfigEditor


def read_json(path, filename):
    with open(os.path.join(path, "ta", filename)) as file:
        res = json.load(file)
        file.close()
    return res


@click.command()
@click.option("--init", nargs=2, type=str, help="Init TA's work directory")
@click.option("--start", is_flag=True, help="Start")
@click.option("--fetch", is_flag=True, help="Fetch draft.json")
@click.option("--submit", nargs=1, type=str, help="Submit work.json")
def cli(init, start, fetch, submit):
    current_dir = os.getcwd()
    if init:
        apikey, workID = init
        if make.init_work_directory(current_dir):
            ConfigEditor(workID, current_dir)
            CallApi(apikey, current_dir)

    if start:
        if check_draft(current_dir):
            draft = read_json(current_dir, "draft.json")
            workID = read_json(current_dir, "config.json")["workID"]
        work = Work()
        work.draft = draft
        work.path = current_dir
        work.workId = workID
        if work.property_is_ready():
            work.create()
        unzipfile(current_dir)
        list_file = os.listdir(current_dir)
        # click.echo(list_file)
        for file in list_file:
            if "." in file or file == "ta":
                continue
            # click.echo(file)
            os.system(f"code {file}")
            student = StudentData(
                path=work.path, filename=file, draft=work.draft)
            student.prepare_student_data()
            work.write_work(student.ask())

    if submit:
        apikey = submit
        SendData(apikey, current_dir)
