import requests
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir)
from lib.file_management.configeditor import ConfigEditor
from lib.file_management.file_management_lib import WorkEditor



class Api:
    def __init__(self, apikey, path) -> None:
        self.apikey = apikey
        self.path = path
        self.data = ConfigEditor.ishaveconfig(self)
        self.prefix = self.data['prefix']
        self.workID = self.data['workID']
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }
        self.getapi = f"v1/workManagement/{self.workID}/getWorkDraft"
        self.url = self.prefix+self.getapi
        self.postapi = f"v1/workManagement/{self.workID}/submitScores"
        self.posturl = self.prefix+self.postapi

class CallApi(Api):
    def __init__(self, apikey, path) -> None:
        super().__init__(apikey, path)
        self.createworkdraft()
        print()


    def createworkdraft(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            print('Success to access')
            self.data = self.res.json()['workDraft']
            self.writejson(self.data)
            return True
        else:
            print(self.res.status_code)
            print(self.res.json()['message'])
            return False


    def writejson(self, data) -> None:
        with open(os.path.join(self.path, 'ta', "draft.json"), "w") as create:
            json.dump(data, create)
        print("workDraft.json file has been created")


class SendData(Api):
    def __init__(self, apikey, path) -> None:
        super().__init__(apikey, path)
        self.getworkDraft()
        

    def getworkDraft(self):
        work = WorkEditor.read_filework(self, self.path)
        send = requests.post(self.posturl, headers=self.hparameter, json=json.loads(work))
        if send.status_code == 200:
            print('Sending data success')
        else:
            print(send.status_code)
            print(send.json())

            
if __name__ == '__main__':
    CallApi('K4nPEs7RhhCzcjdlvr3X==', r'C:\vs\ta\TA-CLI\testypath')