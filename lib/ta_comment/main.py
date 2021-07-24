from check_comment import TAComment
import os
import json
def ta_comment(path):
    std_list = os.listdir(path)
    comments = {"comments":[]}
    container = {}
    traceback = ""
    for studir in std_list:
        container[studir] = []
        for directory, subdirectories, files in os.walk(os.path.join(path,studir)):
            for file in files:
                with open(os.path.join(directory, file),"r") as readfile:
                    filedata = readfile.readlines()
                TA = TAComment(filedata)
                container[studir].append({file:TA.run()}) 
                traceback += "=========================\n"
                traceback += f"{studir}  {file}\n"
                traceback += "=========================\n"
                traceback += TA.out
    print(traceback)      
    return json.dumps(container,indent=3)

