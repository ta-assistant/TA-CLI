import json
import os
import shutil


class SaveApiKey:

    def save(self, apikey):
        if os.path.exists(os.path.join(os.path.expanduser("~"), 'key')):
            if self.exsitapikey():
                print('Already Login')
                choose = input('Do you want login again[y/n]: ')
                if choose == 'y' or choose == 'Y':
                    self.writeapikey(apikey)
                    print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been written.")
                elif choose == 'n' or choose == 'N':
                    print('Decline to login')
                else:
                    print('!!!Invaild Answer!!!')
            else:
                self.writeapikey(apikey)
                print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been written.")
        else:
            os.mkdir(os.path.join(os.path.expanduser("~"), 'key'))
            print(os.path.join(os.path.expanduser("~"), 'key')+'has been created')
            self.writeapikey(apikey)
            print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been created.")

    def readapikey(self):
        with open(os.path.join(os.path.expanduser("~"), 'key', "taconfig.json"), "r") as r:
            data = json.load(r)
        return data['apikey']

    def writeapikey(self, apikey):
        data = {'apikey' : apikey}
        with open(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json'), "w") as wri:
            json.dump(data, wri)
            wri.close()

    def exsitapikey(self):
        if os.path.exists(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')):
            return True
        else:
            return False

    def removeapikey(self):
        try:
            shutil.rmtree(os.path.join(os.path.expanduser("~"), 'key'))
        except OSError:
            print("Deletion of the directory %s failed" % os.path.join(os.path.expanduser("~"), 'key'))
        else:
            print("Deletion of the directory %s success" % os.path.join(os.path.expanduser("~"), 'key'))

