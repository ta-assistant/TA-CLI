import os, json
import requests
from lib.file_management.config_editor import *
from lib.file_management.file_management_lib import WorkEditor
from lib.file_management.create_apikeyfile import *


class Api:
    def __init__(self, path) -> None:
        self.path = path
        self.apikey = readapikey()
        self.data = readconfig(self.path)
        self.prefix = self.data['prefix']
        self.workID = self.data['workId']
        self.hparameter = {'Authorization': self.apikey,
                           'Content-Type': 'application/json'
                           }
        self.list_api = {"getworkdraft" : { "endpoint" : "v1/workManagement/{self.workID}/getWorkDraft",
                                            "method" : "GET"
                                            },
                        "submitscore" : {   "endpoint" : "v1/workManagement/{self.workID}/submitScores",
                                            "method" : "POST"
                        }
                        }
        self.getapi = self.list_api['getworkdraft']['endpoint']
        self.url = self.prefix+self.getapi
        self.postapi = self.list_api['submitscore']['endpoint']
        self.posturl = self.prefix+self.postapi

    def api_massage(self):
        out = "  API Request \n\n"
        for i in self.res.json().items():out += f"  * {i[0]} : {i[1]} \n"
        return out

class CallApi(Api):
    def __init__(self, path) -> None:
        super().__init__(path)
        
    def fetch(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            massage = self.res.json()["message"]
            self.data = self.res.json()['workDraft']
            return self.data
        elif self.res.status_code != 500 and self.res.status_code != 503 and self.res.status_code != 501 and self.res.status_code != 502:
            return False
        else:
            return False
            
    def createworkdraft(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            massage = self.res.json()["message"]
            self.data = self.res.json()['workDraft']
            self.writejson(self.data)
            return True
        elif self.res.status_code != 500 and self.res.status_code != 503 and self.res.status_code != 501 and self.res.status_code != 502:
            return False
        else:
            return False

    def writejson(self, data) -> None:
        draft_path = os.path.join(self.path, 'ta', "draft.json")
        with open(draft_path, "w") as create:
            json.dump(data, create)

class SendData(Api):
    def __init__(self, path) -> None:
        super().__init__(path)
        self.getworkDraft()

    def getworkDraft(self):
        work = WorkEditor.read_filework(self, self.path)
        send = requests.post(
            self.posturl, headers=self.hparameter, data=json.dumps(work))
        if send.status_code == 200:
            return True
        elif send.status_code != 500 and send.status_code != 503 and send.status_code != 501 and send.status_code != 502:
            return False
        else:
            return False
