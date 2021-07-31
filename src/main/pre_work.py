from lib.file_management import WorkEditor
from lib.cli_displayed import display_status_symbol
import os

class Work(WorkEditor):
    def __init__(self) -> None:
        super().__init__()
        self.__workId_state = False
        self.__path_state = False
        self.__draft_state = False
        self.__path = None
        self.__workId = None
        self.__draft = None

    # propert
    @property
    def path(self):
        return self.__path

    @property
    def workId(self):
        return self.__workId

    @property
    def draft(self):
        return self.__draft

    @property
    def path_state(self):
        return self.__path_state

    @property
    def workId_state(self):
        return self.__workId_state

    @property
    def draft_state(self):
        return self.__draft_state

    # setter
    @path.setter
    def path(self, value):
        if os.path.exists(str(value)):
            self.__path = value
            self.__path_state = True
        else:
            print("Invalid Path")

    @workId.setter
    def workId(self, value):
        self.__workId = value
        self.__workId_state = True 

    @draft.setter
    def draft(self, value):
        try:
            filedraft = value["fileDraft"]
            outputdraft = value["outputDraft"]
            if "studentId" in outputdraft and "score" in outputdraft:
                 self.__draft = value
                 self.__draft_state = True
            else:
                display_status_symbol(1,1,"Invalid draft: draft not follow the requriment.")
        except KeyError:
            display_status_symbol(1,1,"Invalid draft: Key error.")

    def property_is_ready(self):
        return self.__draft_state and self.__workId_state and self.__path_state

    def create(self):
        return self.create_file_work()

    def create_file_work(self):
        return super().create_file_work(self.__path,self.__workId,self.__draft)

    def write_work(self, stu_data: dict) -> bool:
        return super().write_work(self.__path, stu_data)