import json
import os
import shutil
    

class DirManagement:
    """
    DirManagement
    create and remove directory
    ===============================================

    it make to handle OSError

    Notes
    -----
    All method is a static method you can call with out `()`
    """
    @staticmethod
    def create_dir(path: str, out=True) :
        """
        Parameter
        ---------
            path: str
                path of working work directory

            out: boolean
                select that you want to get a message or not

        Returns
        -------
            boolean
            If it can create directory it will return True, else is return False

        example
        -------
        < Assume you have a setup as /root/dir1 >
        >>> create_dir("/root/dir1/dir2")
        ... Successfully created the directory /root/dir1/dir2
        >>> create_dir("/root/dir1/dir2")
        ... Creation of the directory /root/dir1/dir2 failed
        
        """
        try:
            os.mkdir(path)
        except OSError:
            if out:
                print("Creation of the directory %s failed" % path)
            return False
        else:
            if out:
                print("Successfully created the directory %s " % path)
            return True

    @staticmethod
    def remove_dir(path: str):
        """
        Parameter
        ---------
            path: str
                path of working work directory
        Returns
        -------
            boolean
            If it can delete directory it will return True, else is return False

        example
        -------
        < Assume you have a setup as /root/dir1/dir2">
        >>> remove_dir("/root/dir1/dir2")
        ... Successfully delete the directory /root/dir1/dir2/dir3
        >>> remove_dir("/root/dir1/dir2")
        ... Deletion of the directory /root/dir1/dir2/dir3 failed
        """
        try:
            shutil.rmtree(path)
        except OSError:
            print("Deletion of the directory %s failed" % path)
            return False
        else:
            print("Successfully deleted the directory %s" % path)
            return True


class WorkEditor:
    """
    WorkEditor
    ==========

    Manage data in work.json
    - change draft
        - reset scores.
    - change workId
    """
    # private

    def _init_work(self, path) -> None:
        with open(os.path.join(path, "ta", "work.json"), 'w') as outfile:
            # init work.json
            json.dump({"workId": "N/A", "workDraft": "N/A",
                       "scores": []}, outfile)
            outfile.close()

    def _check_exits_work(self, path):
        # check that work.json is exists or not
        if os.path.exists(os.path.join(path, "ta", "work.json")):
            return True
        else:
            return False

    def _add_workid(self, path, workId):
        # check that work.json is exists or not
        if self._check_exits_work(path):

            # load data on work.json keep in var data
            with open(os.path.join(path, "ta", "work.json"), "r") as file:
                data = json.load(file)
                file.close()

            # write workid in it
            with open(os.path.join(path, "ta", "work.json"), "w") as file:
                data["workId"] = str(workId)
                json.dump(data, file)
                file.close()

            # displayed
            print(f" |-[*] Your workId is \'{workId}\'")

    def _add_draft(self, path, draft):
        # check that work.json is exists or not
        if self._check_exits_work(path):
            with open(os.path.join(path, "ta", "work.json"), "r") as file:
                data = json.load(file)
                file.close()
            with open(os.path.join(path, "ta", "work.json"), "w") as file:
                data["workDraft"] = draft
                json.dump(data, file)
                file.close()
            print(" |-[*] draft has been written to work.json")
    
    def _check_work_draft(self,path,draft):
        workDraft = self.read_filework(path)
        if draft == workDraft["workDraft"]:
            return False
        else:
            os.remove(os.path.join(path,"ta","work.json"))
            return True

    # public

    def read_filework(self, path):
        with open(os.path.join(path, 'ta', 'work.json')) as r:
            return json.load(r)

    def create_file_work(self, path, workId, draft):
        """
        Create work.json and add draft and workid into it

        parameter
        ---------
        path: string
            work directory path
        
        workId: int
            workid from SERVER

        draft: dict(json)
            draft that have fileDraft and outputdraft need to be form of json
            ex. {"fileDraft": 
                    "{studentId}_test.zip", 
                "outputDraft": 
                        ["studentId", "param1", "param2", "comment", "score", "scoreTimestamp"]}

        Returns
        -------
        bool: Return true when everythin is ready and work.json hasn't been created and
            false when property is not ready or it's already have work.json but draft in 
            work.json not the same with draft on new parameter
        
        example
        -------
        >>> draft = {"fileDraft": "{studentId}_test.zip", "outputDraft": ["studentId", "param1", "param2", "comment", "score", "scoreTimestamp"]}
        >>> create_file_work("/root/dir1/dir2","123456",draft) 
        ... True
        >>> new_draft = {"fileDraft": "{studentId}_test.zip", "outputDraft": ["studentId", "param3", "param4", "comment", "score", "scoreTimestamp"]}
        >>> create_file_work("/root/dir1/dir2","123456",draft) 
        ... False
        """
        if not self._check_exits_work(path):
            # createing work.json and adding workid and draft into file
            self._init_work(path)
            self._add_workid(path, workId)
            self._add_draft(path, draft)
            return True
        else:
            if self._check_work_draft(path,draft):
                while True:
                    # waiting for file to be deleted
                    if not os.path.exists(os.path.join(path,"ta","work.json")):
                        self.create_file_work()
                        break
            return False

    def write_work(self, path, stu_data: dict) :
        """
        add student data to work.json

        parameter
        ---------
        path: string
            work directory path

        stu_data: dict
            list of student data (should ordered) and need to follow form in draft.json :)

        example
        -------
        >>> stu_data = {"studentId":"123456789", "param1":"2", "param2":"3", "comment":"4", "score":5.0, "scoreTimestamp":555555555555}
        >>> write_work("/root/dir1/dir2", stu_data: dict)
        
        $ cat ~/ta/work.json
        {
            "workId": "testWork2",
            "workDraft": {
                "fileDraft": "{studentId}_test.zip",
                "outputDraft": [
                "studentId",
                "param1",
                "param2",
                "comment",
                "score",
                "scoreTimestamp"
                ]
            },
            "scores": [
                {
                "scoreTimestamp": 555555555555,
                "studentId": "123456789",
                "param1":"2",
                "param2":"3",
                "comment":"4",
                "score":5.0
                }
            ]
        }

        """
        # write data to work.json
        with open(os.path.join(path, "ta", "work.json"), "r+") as file:
            data = json.load(file)
            data["scores"].append(stu_data)
            file.seek(0)

            # change dict to json and write it in work.json
            json.dump(data, file, indent=2)

            # message out
            print(str(stu_data) + " has been written down in " +
                  os.path.join(path, "ta", "work.json"))
            file.close()

    
            

            
            
