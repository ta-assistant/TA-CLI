import os
import json


class ConfigEditor:
    """
    ConfigEditor
    create, read, checkexist and check data of config.json
    ====================================================

    It make for handle config.json file
    
    """
    def __init__(self, workID=None, path=None, prefix='https://ta-api.sirateek.dev/') -> None:
        """
        Parameter
        -------------------------------------
            workID : String
                Name of work did you want to do.
            
            path : String
                Directory to create of ta/config.json

            prefix : String
                Url form of api address
        
        ==========================================
        """
        self.id = workID
        self.path = path
        self.pre = prefix

    def writeconfig(self) -> None:
        """
        Function to create, wirte data of config.josn
        """
        data = {"prefix": f"{self.prefix}",
                "apikeydir": os.path.join(os.path.expanduser("~"), 'key')}
        with open(os.path.join(self.path, 'ta', 'config.json'), "w") as wri:
            json.dump(data, wri)

    def readconfig(self) -> dict:
        """
        Function to read config.json
        ====================================================

        Return:
            Dictionary(dict of converting json string)
        """
        with open(os.path.join(self.path, 'ta', "config.json"), "r") as r:
            data = json.load(r)
        return data

    def ishaveconfig(self):
        """
        Function to check exist of config.json if not exist will recreate config.json 
        """
        check = os.path.isfile(os.path.join(self.path, 'ta', 'config.json'))
        if check == True:
            self.checkdata()
        else:
            self.writeconfig()

    def checkdata(self):
        """
        Function to check data inside config.json if data is invalid will recreate config.json
        =======================================================================================

        Return:
            None
        """
        data = self.readconfig()
        if data['workId'] == '':
            self.writeconfig()
        else:
            return
