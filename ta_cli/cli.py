import click
import os
import sys
import json

from click.decorators import command
from src.main.run_work import run_work
from src.build import make
from lib.file_management.extract import unzipfile
from lib.function_network.func_network import CallApi, SendData
from lib.file_management.configeditor import ConfigEditor
from lib.file_management.createapikeyfile import SaveApiKey

current_dir = os.getcwd()


def read_json(path, filename):
    with open(os.path.join(path, "ta", filename)) as file:
        res = json.load(file)
        file.close()
    return res


@click.group()
def cli():
    pass


@cli.command()
@click.argument("apikey", type=str)
def login(apikey):
    """Login"""
    SaveApiKey().save(apikey)


@cli.command()
@click.argument("work_id", type=str)
def init(work_id):
    """Init TA's work directory
    Args:
        workID (str): Work's ID
    """
    make.init_work_directory(current_dir, work_id)


@cli.command()
def start(VSCODE,ONEBYONE):
    """Start working on TA directory"""
    run_work(current_dir)


@cli.command()
def fetch():
    """Fetch draft.json"""
    pass


@cli.command()
def submit():
    """Submit"""
    SendData(current_dir)
