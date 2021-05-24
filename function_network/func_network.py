import requests
import json
import os
import sys
sys.path.insert(1,f"{os.getcwd()}/function_network")
from config import *




class Call_api:
    def __init__(self, apikey, id) -> None:
        self.apikey = apikey
        self.id = id
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }

        self.getapi = f'v1/workManagement/{id}/getWorkDraft'
        self.url = f'{prefix}{self.getapi}'



    def createworkdraft(self):
        self.res = requests.get(self.url, headers=self.hparameter)
        if self.res.status_code == 200:
            print('Success to access')    
            self.data = self.res.json()['workDraft']
            WriteWorkdaft(self.data)
        else:
            print(self.res.json()['message'])


class WriteWorkdaft:
    def __init__(self, workdaft) -> None:
        self.work = workdaft
        self.create_work()

    def create_work(self, work) -> None:
        if not os.path.exists(os.getcwd()+'/function_network'):
            try:
                os.makedirs(os.getcwd()+'/function_network')
            except Exception as e:
                print(e)
                raise
        with open(os.path.join(os.getcwd()+'/function_network', "workDraft.json"), "w") as create:
            json.dump(self.work, create)
        print("workDraft.json file has been created")

class SendData:
    def __init__(self, apikey, id) -> None:
        self.apikey = apikey
        self.id = id
        self.hparameter = { 'Authorization': self.apikey,
                'Content-Type': 'application/json',
        }


        self.postapi = f'v1/workManagement/{id}/submitScores'
        self.posturl = f'{prefix}{self.postapi}'
        self.getworkDraft()
        

    def getworkDraft(self):
        with open(os.getcwd()+'/function_network/ex_workdraft.json') as r:
            workdraft = json.load(r)
        send = requests.post(self.posturl, headers=self.hparameter, json=workdraft)
        if send.status_code == 200:
            print('Sending data success')
        else:
            print(send.status_code)
            print(send.json())

            
if __name__ == "__main__":
    Call_api('K4nPEs7RhhCzcjdlvr3X==', 'testWork2')
    SendData('K4nPEs7RhhCzcjdlvr3X==', 'testWork2')
