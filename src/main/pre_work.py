from lib.file_management import WorkEditor
from lib.cli_displayed import display_status_symbol
import os

class Work(WorkEditor):
    def __init__(self) -> None:
        super().__init__()
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

    # setter
    @path.setter
    def path(self, value):
        if os.path.exists(str(value)):
            self.__path = value
        else:
            print("Invalid Path")

    @workId.setter
    def workId(self, value):
        self.__workId = value

    @draft.setter
    def draft(self, value):
        try:
            filedraft = value["fileDraft"]
            outputdraft = value["outputDraft"]
            if "studentId" in outputdraft and "score" in outputdraft:
                 self.__draft = value
        except KeyError:
            pass

    def property_is_ready(self):
        if self.__path == None:
            return False
        if self.__draft == None:
            return False
        if self.__workId == None:
            return False
        return True

    def create(self):
        return self.create_file_work()

    def create_file_work(self):
        return super().create_file_work(self.__path,self.__workId,self.__draft)

    def write_work(self, stu_data: dict) -> bool:
        return super().write_work(self.__path, stu_data)