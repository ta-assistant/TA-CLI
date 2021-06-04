import json
import os

class SaveApiKey:

    def save(self, apikey):
        if os.path.exists(os.path.join(os.path.expanduser("~"), 'key')):
            data = {'apikey' : apikey}
            with open(os.path.join(os.path.expanduser("~"), 'key', 'apik.json'), "w") as wri:
                json.dump(data, wri)
        else:
            os.mkdir(os.path.join(os.path.expanduser("~"), 'key'))
            data = {'apikey' : apikey}
            with open(os.path.join(os.path.expanduser("~"), 'key', 'apik.json'), "w") as wri:
                json.dump(data, wri)

    def readapikey(self):
        with open(os.path.join(os.path.expanduser("~"), 'key', "apik.json"), "r") as r:
            data = json.load(r)
        return data['apikey']

