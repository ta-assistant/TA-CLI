import click
import os
import sys
from src.build import make
from src.main.draft_check import check_draft
from src.main.student_data import StudentData


@click.command()
@click.option("--init", is_flag=True, help="Create TA directory")
@click.option("--start", is_flag=True, help="Start")
@click.option("--fetch", is_flag=True, help="Fetch draft.json")
def cli(init, start, fetch):
    current_dir = os.getcwd()
    if init:
        make.init_work_directory(current_dir)
    elif start:
        click.echo(current_dir)
        if check_draft(current_dir):
            click.echo("yes")
            list_student_dir = os.listdir(current_dir)
            for folder in list_student_dir:
                if folder == "ta" or folder == ".DS_Store":
                    continue
                bashcommand = f"code {folder}"
                os.system(bashcommand)

                # student_data = StudentData(current_dir, folder)
                # student_data.prepare_student_data()
                # student_data.ask()
        else:
            return
    elif fetch:
        pass
