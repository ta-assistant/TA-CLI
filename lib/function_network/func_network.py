import os, sys, inspect, json
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from file_management.createapikeyfile import SaveApiKey
from file_management.file_management_lib import WorkEditor
from file_management.configeditor import ConfigEditor
import requests
import json
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir)


class Api:
    def __init__(self, path) -> None:
        self.path = path
        self.apikey = SaveApiKey.readapikey(self)
        self.data = ConfigEditor.readconfig(self)
        self.prefix = self.data['prefix']
        self.workID = self.data['workId']
        self.hparameter = {'Authorization': self.apikey,
                           'Content-Type': 'application/json',
                           }
        self.getapi = f"v1/workManagement/{self.workID}/getWorkDraft"
        self.url = self.prefix+self.getapi
        self.postapi = f"v1/workManagement/{self.workID}/submitScores"
        self.posturl = self.prefix+self.postapi

    

class CallApi(Api):
    def __init__(self, path) -> None:
        super().__init__(path)
        
    def api_massage(self):
        out = "  API Request \n\n"
        for i in self.res.json().items():out += f"  * {i[0]} : {i[1]} \n"
        return out

    def fetch(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            massage = self.res.json()["message"]
            self.data = self.res.json()['workDraft']
            return self.data
        elif self.res.status_code != 500 and self.res.status_code != 503 and self.res.status_code != 501 and self.res.status_code != 502:
            print(self.res.status_code)
            print(self.res.json())
        else:
            print(self.res.status_code)
            print('!!!SERVER HAVE ISSUE!!!')
            print("PLEASE TRY AGAIN LATER")
            
    def createworkdraft(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            massage = self.res.json()["message"]
            self.data = self.res.json()['workDraft']
            self.writejson(self.data)
            return True
        elif self.res.status_code != 500 and self.res.status_code != 503 and self.res.status_code != 501 and self.res.status_code != 502:
            print(self.res.status_code)
            print(self.res.json())
            return False
        else:
            print(self.res.status_code)
            print('!!!SERVER HAVE ISSUE!!!')
            print("PLEASE TRY AGAIN LATER")
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
            for i in send.json().items():print(i[0],":",i[1])
        elif send.status_code != 500 and send.status_code != 503 and send.status_code != 501 and send.status_code != 502:
            for i in send.json().items():print(i[0],":",i[1])
        else:
            print('!!!SERVER HAVE ISSUE!!!')
            print("PLEASE TRY AGAIN LATER")
