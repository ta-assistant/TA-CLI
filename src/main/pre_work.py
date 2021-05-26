from lib.file_management.file_management_lib import WorkEditor
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(0, parentdir)


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
        self.__path = value

    @workId.setter
    def workId(self, value):
        self.__workId = value

    @draft.setter
    def draft(self, value):
        try:
            draft = value["workDraft"]["fileDraft"]
            draft = value["workDraft"]["outputDraft"]
            self.__draft = value["workDraft"]
        except KeyError:
            print("Invalid draft.")

    def property_is_ready(self):
        if self.__path == None:
            return False
        if self.__draft == None:
            return False
        if self.__workId == None:
            return False
        return True

    def create(self):
        self.create_file_work()
        self.add_draft()
        self.add_workid()

    def create_file_work(self):
        return super().create_file_work(self.__path)

    def add_workid(self):
        return super().add_workid(self.__path, self.__workId)

    def add_draft(self):
        return super().add_draft(self.__path, self.__draft)

    def write_work(self, stu_data: dict) -> bool:
        return super().write_work(self.__path, stu_data)