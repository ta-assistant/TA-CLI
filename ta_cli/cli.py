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
from lib.function_network.func_network import CallApi


@click.command()
@click.option("--init", nargs=2, type=str, help="Init TA's work directory")
@click.option("--start", is_flag=True, help="Start")
@click.option("--fetch", is_flag=True, help="Fetch draft.json")
def cli(init, start, fetch):
    current_dir = os.getcwd()
    if init:
        apikey, workid = init
        if make.init_work_directory(current_dir):
            fetch_draft = CallApi(apikey, workid, current_dir)
            # with open(os.path.join(current_dir, "ta", "config.txt"), "r+") as configfile:
            #     configfile.write(f"\nworkID = {workid}\napiKey = {apikey}")
            #     configfile.close()
    if start:
        if check_draft(current_dir):
            with open(os.path.join(current_dir, "ta", "draft.json")) as file:
                draft = json.load(file)
                file.close()
            work = Work()
            work.draft = draft
            work.path = current_dir
            click.echo(current_dir)
            work.workId = 6310546031
            if work.property_is_ready():
                unzipfile(current_dir)
                work.create()
                list_file = os.listdir(current_dir)
                command = f"code {current_dir}"
                os.system(command)
                for file in list_file:
                    if "." in file:
                        continue
                    student = StudentData(
                        path=work.path, filename=file, draft=work.draft)
                    student.prepare_student_data()
                    work.write_work(student.ask())
