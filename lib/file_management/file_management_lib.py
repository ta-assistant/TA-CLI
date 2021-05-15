import os

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
        
