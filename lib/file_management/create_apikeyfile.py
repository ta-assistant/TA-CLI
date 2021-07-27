import json
import os
import shutil


class SaveApiKey:
    """
    SaveApiKey
    create, read, check exist, remove taconfig.json
    ==================================================

    It make for handle all feature to need for create file to save api's key

    Note:
        All function in this file isn't static method so you need to call with '()'
    """

    def save(self, apikey):
        """
        Parameter
        -------------------------------------
            apikey:
                It is a personal api key to access tp api
        =================================================

        Return:
            None
        ===================================================

        Example:
            <assume taconfig doesn't exist>
            >>> SaveApiKey().save('test')
            User/key/taconfig.json has been created
            <assume taconfig does exist>
            >>> SaveApiKey().save('test')
            Already Login
            Do you want login again[y/n]:
            >>> Y
            User/key/taconfig.json has been written
            <assume taconfig does exist>
            >>> SaveApiKey().save('test')
            Already Login
            Do you want login again[y/n]:
            >>> N
            Decline to login
            <assume taconfig does exist>
            >>> SaveApiKey().save('test')
            Already Login
            Do you want login again[y/n]:
            >>> L
            '!!!Invaild Answer!!!'
        """
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
            print(os.path.join(os.path.expanduser("~"), 'key')+' has been created')
            self.writeapikey(apikey)
            print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been created.")

    def readapikey(self):
        """
        Function to read data in taconfig.json
        ---------------------------------------------------'

        Return:
            String
        """
        with open(os.path.join(os.path.expanduser("~"), 'key', "taconfig.json"), "r") as r:
            data = json.load(r)
        return data['apikey']

    def writeapikey(self, apikey):
        """
        Function to create taconfig.json
        ===================================

        Return:
            None
        """
        data = {'apikey' : apikey}
        with open(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json'), "w") as wri:
            json.dump(data, wri)
            wri.close()

    def exsitapikey(self):
        """
        Function to check exist tacongfig.json
        ============================================
        
        Return:
            Boolean
        """
        if os.path.exists(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')):
            return True
        else:
            return False

    def removeapikey(self):
        """
        Function to remove folder key(directtory of taconfig.josn)
        ==================================================================

        Return:
            None
        ==================================================================

        Example:
            <Assume didn't error>
            >>> SaveApiKey().removeapikey()
            Deletion of the directory User/key success
            <Assume did error>
            >>> SaveApiKey().removeapikey()
            Deletion of the directory User/key failed
        """
        try:
            shutil.rmtree(os.path.join(os.path.expanduser("~"), 'key'))
        except OSError:
            print("Deletion of the directory %s failed" % os.path.join(os.path.expanduser("~"), 'key'))
        else:
            print("Deletion of the directory %s success" % os.path.join(os.path.expanduser("~"), 'key'))

