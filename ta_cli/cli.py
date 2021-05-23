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


@click.command()
@click.option("--init", is_flag=True, help="Create TA directory")
@click.option("--start", is_flag=True, help="Start")
@click.option("--fetch", is_flag=True, help="Fetch draft.json")
def cli(init, start, fetch):
    current_dir = os.getcwd()
    if init:
        make.init_work_directory(current_dir)
    elif start:
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
                for file in list_file:
                    if "." in file:
                        continue
                    command = f"code {file}"
                    os.system(command)
                    student = StudentData(
                        path=work.path, filename=file, draft=work.draft)
                    student.prepare_student_data()
                    work.write_work(student.ask())
