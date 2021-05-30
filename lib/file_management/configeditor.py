import os
import json

class ConfigEditor:
    def __init__(self, workID, path) -> None:
        self.id = workID
        self.path = path
        self.writeconfig()
        

    def writeconfig(self) -> None:
        data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workID" : self.id}
        with open(os.path.join(self.path, 'ta', 'config.json'), "w") as wri:
            json.dump(data, wri)
        print('confix.json has been create')

    def readconfig(self) -> tuple:
        with open(os.path.join(self.path, 'ta', "config.json"), "r") as r:
            data = json.load(r)
        return data["prefix"], data["workID"]
