import requests
import json
import os


class Call_api:
    def __init__(self, apikey, id) -> None:


        self.hparameter = { 'Authorization': apikey,
                'Content-Type': 'application/json',
        }

        self.id = id
        self.prefix = "https://ta-api.sirateek.dev/"
        self.apipath = f'v1/workManagement/{self.id}/getWorkDraft'
        self.url = f'{self.prefix}{self.apipath}'

        self.res = self.response()
        self.createworkdraft()

    def response(self):
        res = requests.get(self.url, headers=self.hparameter)
        return res

    def createworkdraft(self):
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

    def create_work(self) -> None:
        if not os.path.exists(os.getcwd()+'/function_network'):
            try:
                os.makedirs(os.getcwd()+'/function_network')
            except Exception as e:
                print(e)
                raise
        with open(os.path.join(os.getcwd()+'/function_network', "workDraft.json"), "w") as create:
            json.dump(self.work, create)
        print("workDraft.json file has been created")

class SendData(Call_api):
    def __init__(self, apikey, id) -> None:
        super().__init__(apikey, id)
        self.prefix = "https://ta-api.sirateek.dev/"
        self.apipath = f'v1/workManagement/{self.id}/submitScores'
        self.posturl = f'{self.prefix}{self.apipath}'
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
