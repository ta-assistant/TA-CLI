import os, json
import requests
from lib.file_management.config_editor import *
from lib.file_management.file_management_lib import WorkEditor
from lib.file_management.create_apikeyfile import *


class Api:
    """
    Api
    Create a base code that is required.
    """
    def __init__(self, path) -> None:
        """
        Parameter
        -------------------------------------------------------
        path:
            Directory of config.josn file
        """
        self.path = path
        self.apikey = readapikey()
        self.data = readconfig(self.path)
        self.prefix = self.data['prefix']
        self.workID = self.data['workId']
        self.hparameter = {'Authorization': self.apikey,
                           'Content-Type': 'application/json'
                           }
        self.list_api = {"getworkdraft" : { "endpoint" : f"v1/workManagement/{self.workID}/getWorkDraft",
                                            "method" : "GET"
                                            },
                        "submitscore" : {   "endpoint" : f"v1/workManagement/{self.workID}/submitScores",
                                            "method" : "POST"
                        }
                        }
        self.getapi = self.list_api['getworkdraft']['endpoint']
        self.url = self.prefix+self.getapi
        self.postapi = self.list_api['submitscore']['endpoint']
        self.posturl = self.prefix+self.postapi

    def api_massage(self):
        """
        Function for reading response from api
        ===========================================

        Return
        --------------------------------------------
            json object
            All the response from api in type of json
        """
        return self.res.json()

class CallApi(Api):
    """
    CallApi
    call api to get a draft.json
    """
    def __init__(self, path) -> None:
        """
        Parameter
        -------------------------------
        path:
            directory of TA-CLI
        """
        super().__init__(path)
        
    def fetch(self):
        """
        Function of calling api for fetch draft from api
        =================================================

        Return
        -------------------------------------------------
            boolean:
                if call api success will return True but fail will return False
        """
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
        """
        Function of calling api for pull draft from api to local
        ========================================================

        Return
        -------------------------------------------------------
            boolean:
                if call api success will return True but fail will return False
        """
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
        """
        Function for write from api to draft.json
        """
        draft_path = os.path.join(self.path, 'ta', "draft.json")
        with open(draft_path, "w") as create:
            json.dump(data, create)

class SendData(Api):
    """
    SendData
    send data from work.josn to server
    """
    def __init__(self, path) -> None:
        """
        Parameter
        -------------------------------
        path:
            directory of TA-CLI
        """
        super().__init__(path)
        self.getworkDraft()

    def getworkDraft(self):
        """
        Function for read data form work.json abnd send data to api
        ================================================================

        Return
        ----------------------------------------------------------------
            boolean:
                if sending data success will return True but fail will return False
        """
        work = WorkEditor.read_filework(self, self.path)
        self.res = requests.post(
            self.posturl, headers=self.hparameter, data=json.dumps(work))
        if self.res.status_code == 200:
            return True
        elif self.res.status_code != 500 and self.res.status_code != 503 and self.res.status_code != 501 and self.send.status_code != 502:
            return False
        else:
            return False

