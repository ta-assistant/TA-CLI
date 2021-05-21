import requests
import json

class Path:
    def find_path(start, api_path):
        return f"{start}{api_path}"


class Call_api(Path):
    def __init__(self, apikey, workid, prefix="https://google.com") -> str:
        
        self.hparameter = { 'Authorization': apikey,
                    'Content-Type': 'application/json',
        }

        self.dparameter = {
            "workID": workid
        }

        self.prefix = prefix

        self.url = Path.find_path(self.prefix, "/v1/getWorkDraft/")

    def response(self):
        self.active = requests.get(self.url, headers=self.hparameter, data=self.dparameter)
        return self.active

if __name__ == "__main__":
    api_called = Call_api('ApiKey', 'testWork')
    print(api_called.response())


