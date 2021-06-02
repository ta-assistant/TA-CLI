import json
import os

class SaveApiKey:

    def __init__(self, path) -> None:
        self.path = path

    def save(self, apikey):
        data = {'apikey' : apikey}
        with open(os.path.join(self.path, 'ta', 'apik.json'), "w") as wri:
            json.dump(data, wri)

    def readapikey(self):
        with open(os.path.join(self.path, 'ta', "apik.json"), "r") as r:
            data = json.load(r)
        return data


if __name__ == '__main__':
    a = SaveApiKey(r'C:\vs\ta\TA-CLI\testypath')
    a.save('K4nPEs7RhhCzcjdlvr3X==')