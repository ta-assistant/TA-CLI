import json
import os

class SaveApiKey:

    def __init__(self, path) -> None:
        self.path = path

    def save(self, apikey):
        data = {'apikey' : apikey}
        os.mkdir(os.path.join(self.path, 'key'))
        with open(os.path.join(self.path, 'key', 'apik.json'), "w") as wri:
            json.dump(data, wri)

    def readapikey(self):
        with open(os.path.join(self.path, 'key', "apik.json"), "r") as r:
            data = json.load(r)
        return data

