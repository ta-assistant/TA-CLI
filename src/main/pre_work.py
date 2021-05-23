import os,sys,inspect
from posix import PRIO_PGRP
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0,parentdir)

from lib.file_management.file_management_lib import WorkEditor

class Work(WorkEditor):
    def __init__(self) -> None:
        super().__init__()
        self.path = None
        self.workId = None
        self.draft = None

    # propert        
    @property
    def path(self):
        return self.path
    @property
    def workId(self):
        return self.workId
    @property
    def draft(self):
        return self.draft
    # setter
    @path.setter
    def path(self,value):
        if os.path.exists(value):
            print("Invalid path")
        else:
            self.path = value
    @workId.setter
    def workId(self,value):
        self.workId = value
    @draft.setter
    def draft(self,value):
        try:
            draft = value["workDraft"]["fileDraft"]
            draft = value["workDraft"]["outputDraft"]
            self.draft = value["workDraft"]
        except KeyError:
            print("Invalid draft.")

    def property_is_ready(self):
        if self.path == None:
            return False
        if self.draft == None:
            return False
        if self.workId == None:
            return False
        return True

    def create(self):
        self.create_file_work()
        self.add_draft()
        self.add_workid()

    def create_file_work(self):
        return super().create_file_work(self.path)   
    
    def add_workid(self):
        return super().add_workid(self.path, self.workId)
    
    def add_draft(self):
        return super().add_draft(self.path, self.draft)
    
    def write_work(self, stu_data: dict) -> bool:
        return super().write_work(self.path, stu_data)
        
