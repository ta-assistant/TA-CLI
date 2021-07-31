import click
import os
import json

from src.main.run_work import run_work
from src.build import make
from lib.cli_displayed import display_api_status_message
from lib.file_management import save_api_key
from lib.function_network import SendData


current_dir = os.getcwd()


def read_json(path, filename):
    with open(os.path.join(path, "ta", filename)) as file:
        res = json.load(file)
        file.close()
    return res


def ask_user(msg):
    while True:
        res = input(msg)
        if res.lower() == "y":
            return True
        elif res.lower() == "n":
            return False
        else:
            click.echo("Invalid input")


@click.group()
def cli():
    pass


@cli.command()
@click.option("--apikey", required=True, type=str)
def login(apikey):
    """Login"""
    save_api_key(apikey)


@cli.command()
@click.option("--workid", required=True, type=str)
def init(workid):
    """Init TA's work directory
    Args:
        workID (str): Work's ID
    """
    make.init_work_directory(current_dir, workid)


@cli.command()
def start():
    """Start working on TA directory"""
    openvs = ask_user("Do you want to open vscode?(y/n): ")
    fbf = ask_user("Folder by folder?(y/n): ") if openvs else False
    run_work(current_dir, openvs, fbf)


@cli.command()
def fetch():
    """Fetch draft.json"""
    pass


@cli.command()
def submit():
    """Submit"""
    if os.path.exists(os.path.join(current_dir,"ta","work.json")):
        display_api_status_message((SendData(current_dir).api_massage()),0) 
    else:
        print("You don't have work.json to submit")
