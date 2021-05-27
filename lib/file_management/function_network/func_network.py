import requests
import json
import os
from configparser import ConfigParser

class ReadFile:
    def fileread(self, path, filename):
        if filename == 'config.txt':
            config = ConfigParser() 
            configFilePath = os.path.join(path ,'ta', filename)
            config.read_file(open(configFilePath))
            return config.get("CONFIG","prefix")
        else:
            with open(os.path.join(path, 'ta', filename)) as r:
                return r.read()

                
class CallApi(ReadFile):
    def __init__(self, apikey, workID, path) -> None:
        self.apikey = apikey
        self.path = path
        self.prefix = self.fileread(self.path,'config.txt')
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }

        self.getapi = f"v1/workManagement/{workID}/getWorkDraft"
        self.url = self.prefix+self.getapi
        self.createworkdraft()
        print()


    def createworkdraft(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            print('Success to access')
            self.data = self.res.json()['workDraft']
            self.writejson(self.data)
        else:
            print(self.res.status_code)
            print(self.res.json()['message'])


    def writejson(self, data) -> None:
        with open(os.path.join(self.path, 'ta', "draft.json"), "w") as create:
            json.dump(data, create)
        print("workDraft.json file has been created")


class SendData(ReadFile):
    def __init__(self, apikey, workID, path) -> None:
        self.apikey = apikey
        self.path = path
        self.prefix = self.fileread(self.path, 'config.txt')
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }


        self.postapi = f"v1/workManagement/{workID}/submitScores"
        self.posturl = self.prefix+self.postapi
        self.getworkDraft()
        

    def getworkDraft(self):
        work = self.fileread(self.path, 'work.json')
        send = requests.post(self.posturl, headers=self.hparameter, json=json.loads(work))
        if send.status_code == 200:
            print('Sending data success')
        else:
            print(send.status_code)
            print(send.json())

            