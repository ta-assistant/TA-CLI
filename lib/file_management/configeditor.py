import os
import json

class ConfigEditor:
    def __init__(self, workID = None, path = None) -> None:
        self.id = workID
        self.path = path

    def writeconfig(self) -> None:
        data = {"prefix" : "https://ta-api.sirateek.dev/",
                "workID" : self.id,
                "apikeydir" : os.path.join(os.path.expanduser("~"), 'key')}
        with open(os.path.join(self.path, 'ta', 'config.json'), "w") as wri:
            json.dump(data, wri)
        print('confix.json has been create')

    def readconfig(self) -> tuple:
        with open(os.path.join(self.path, 'ta', "config.json"), "r") as r:
            data = json.load(r)
        return data

    def ishaveconfig(self):
        check = os.path.isfile(os.path.join(self.path, 'ta', 'config.json'))
        if check == True:
            self.checkdata()
        else:
            self.writeconfig()
            
    def checkdata(self):
        data = self.readconfig()
        if data['workID'] == '':
            self.writeconfig()
        else:
            return 
        
