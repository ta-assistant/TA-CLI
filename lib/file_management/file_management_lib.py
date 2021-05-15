import os
import shutil

class FileEditor:
    @staticmethod
    def create_file(path,filename) -> str:
        with open(path+filename, 'w') as fp:
             pass
    @staticmethod
    def delete_file(path,filename) -> str:
        if os.path.exists(path+filename):
            os.remove(path+filename)
        else:
            print("The "+path+filename+" does not exist")
        
class DirManagement:
    @staticmethod
    def create_dir(path):
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        
    @staticmethod
    def remove_dir(path):
        try:
            shutil.rmtree(path)
        except OSError:
            print ("Deletion of the directory %s failed" % path)
        else:
            print ("Successfully deleted the directory %s" % path)
                