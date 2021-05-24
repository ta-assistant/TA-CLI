import requests
import json
import os


class CallApi:
    def __init__(self, apikey, workID, path) -> None:
        self.apikey = apikey
        self.path = path
        self.prefix = self.readprefix()
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }

        self.getapi = f"v1/workManagement/{workID}/getWorkDraft"
        self.url = self.prefix+self.getapi
        self.createworkdraft()
        print()
    
    def readprefix(self):
        p = open(os.path.join(self.path, 'ta', 'config.txt'), "r")
        prefix = p.read().split()[2]
        p.close()
        return prefix

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


class SendData:
    def __init__(self, apikey, workID, path) -> None:
        self.apikey = apikey
        self.path = path
        p = open(os.path.join(self.path, 'ta', 'config.txt'), "r")
        self.prefix = p.read().split()[2]
        p.close()
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }


        self.postapi = f"v1/workManagement/{workID}/submitScores"
        self.posturl = self.prefix+self.postapi

        

    def getworkDraft(self):
        with open(os.path.join(self.path, 'ta', 'work.json')) as r:
            workdraft = json.load(r)
        send = requests.post(self.posturl, headers=self.hparameter, json=workdraft)
        if send.status_code == 200:
            print('Sending data success')
        else:
            print(send.status_code)
            print(send.json())

            
if __name__ == "__main__":
    CallApi('K4nPEs7RhhCzcjdlvr3X==', 'testWork2', r'C:\vs\ta\TA-CLI\testypath')
    SendData('K4nPEs7RhhCzcjdlvr3X==', 'testWork2', r'C:\vs\ta\TA-CLI\testypath')
