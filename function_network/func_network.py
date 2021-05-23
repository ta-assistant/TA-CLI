import requests
import json
import os


class Call_api:
    def __init__(self, apikey) -> None:
        

        self.hparameter = { 'Authorization': apikey,
                'Content-Type': 'application/json',
        }


        self.url = "https://ta-api.sirateek.dev/v1/workManagement/testWork/getWorkDraft"

        self.res = self.response()
        self.get_workdraft()

    def response(self):
        res = requests.get(self.url, headers=self.hparameter)
        return res

    def get_workdraft(self):
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
        with open(os.path.join(os.getcwd()+'/function_network', "WorkDaft.json"), "w") as create:
            json.dump(self.work, create)
        print("workDraft.json file has been created")


if __name__ == "__main__":
    Call_api('K4nPEs7RhhCzcjdlvr3X==')

