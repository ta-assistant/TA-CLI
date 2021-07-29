import json
import os
import shutil



def save_api_key(apikey):
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
        if exsitapikey():
            print('Already Login')
            choose = input('Do you want login again[y/n]: ')
            if choose == 'y' or choose == 'Y':
                writeapikey(apikey)
                print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been written.")
            elif choose == 'n' or choose == 'N':
                print('Decline to login')
            else:
                print('!!!Invaild Answer!!!')
        else:
            writeapikey(apikey)
            print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been written.")
    else:
        os.mkdir(os.path.join(os.path.expanduser("~"), 'key'))
        print(os.path.join(os.path.expanduser("~"), 'key')+' has been created')
        writeapikey(apikey)
        print(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json')+" has been created.")

def readapikey():
    """
    Function to read data in taconfig.json
    ---------------------------------------------------'

    Return:
        String
    """
    with open(os.path.join(os.path.expanduser("~"), 'key', "taconfig.json"), "r") as r:
        data = json.load(r)
    return data['apikey']

def writeapikey(apikey):
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

def exsitapikey():
    """
    Function to check exist tacongfig.json
    ============================================
    
    Return:
        Boolean
    """
    return os.path.exists(os.path.join(os.path.expanduser("~"), 'key', 'taconfig.json'))

def removeapikey():
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

