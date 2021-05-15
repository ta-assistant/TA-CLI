from file_management_lib import FileEditor
import os 

class JobWrite(FileEditor):
    def create_file_job(self,path,filename):
        if not os.path.exists(path,filename):
            self.create_file(path,filename)
        print("job.json exits")
    
    def write_job(self):


