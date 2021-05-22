import requests
import json
import os


class Call_api:
    def __init__(self, apikey, workid, prefix="https://google.com") -> None:

        self.hparameter = { 'Authorization': apikey,
                    'Content-Type': 'application/json',
        }

        self.dparameter = {
            "workID": workid
        }

        self.prefix = prefix

        self.url = self.find_path(self.prefix, "/v1/getWorkDraft/")

    def response(self):
        res = requests.get(self.url, headers=self.hparameter, data=self.dparameter)
        return res

    def find_path(self, start, api_path) -> str:
        return f"{start}{api_path}"


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
        with open(os.path.join(os.getcwd()+'/function_network', "Work_daft.json"), "w") as create:
            json.dump(self.work, create)
        print("json file has been created")


if __name__ == "__main__":
    api_called = Call_api('ApiKey', 'testWork')
    print(api_called.response())
    a = {"workDraft": {
        "outputDraft": [
            "a",
            "b",
            "score1"
        ],
        "zipFileDraft": "{a}_{b}.zip"} }
    WriteWorkdaft(a)

