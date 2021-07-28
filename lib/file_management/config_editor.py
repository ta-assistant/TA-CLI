import os
import json


def writeconfig(path=None, workID=None, prefix='https://ta-api.sirateek.dev/') -> None:
    """
    Function to create, wirte data of config.josn
    """
    data = {"prefix": f"{prefix}",
            "workId" : f"{workID}",
            "apikeydir" : os.path.join(os.path.expanduser("~"), 'key')}
    with open(os.path.join(path, 'ta', 'config.json'), "w") as wri:
        json.dump(data, wri)

def readconfig(path) -> dict:
    """
    Function to read config.json
    ====================================================

    Return:
        Dictionary(dict of converting json string)
    """
    with open(os.path.join(path, 'ta', "config.json"), "r") as r:
        data = json.load(r)
    return data

def ishaveconfig(path):
    """
    Function to check exist of config.json if not exist will recreate config.json 
    """
    check = os.path.isfile(os.path.join(path, 'ta', 'config.json'))
    if check == True:
        checkdata(path)
    else:
        writeconfig(path)

def checkdata(path):
    """
    Function to check data inside config.json if data is invalid will recreate config.json
    =======================================================================================

    Return:
        None
    """
    data = readconfig(path)
    if data['workId'] == '':
        writeconfig(path)
    else:
        return
