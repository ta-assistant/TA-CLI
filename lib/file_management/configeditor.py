import os
from configparser import ConfigParser

class ConfigEditor:
    def __init__(self, workID, path) -> None:
        self.id = workID
        self.path = path
        self.writeconfig()
        

    def writeconfig(self) -> None:
        with open(os.path.join(self.path, 'ta', 'config.txt'), "w") as wri:
            wri.write("[CONFIG]\nprefix = https://ta-api.sirateek.dev/")
            wri.write(f'\nworkID = {self.id}')
            print("config.txt has been create")
            wri.close()

    def readconfig(self) -> tuple:
        config = ConfigParser() 
        configFilePath = os.path.join(self.path ,'ta', 'config.txt')
        config.read_file(open(configFilePath))
        return config.get("CONFIG","prefix"), config.get("CONFIG","workID")