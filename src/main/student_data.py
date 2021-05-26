import json
from lib.file_management.file_management_lib import FileEditor, DirManagement, WorkEditor
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
sys.path.insert(0, currentdir)


def inask(question: str) -> str:
    """
    this fnc made for test because we need user input but intest it cant typing itself os it need to call patch module
    but it need to create a sperate function and call it in function that we want to use
    Args:
        question (str): any string
    Returns:
        str: user input
    """
    answer = input(question)
    return answer


class StudentData:
    def __init__(self, path: str, filename: str, draft: dict) -> None:
        """
        init draft 
        draft_file (str) 
        draft_work (list)
        if user did not have draft.json it will return None
        Args:
            path (str): path of work directory
            filename (str): name of student's directory of file
        """
        self.draft_file = draft["fileDraft"]
        self.draft_out = draft["outputDraft"]
        self.pre_data = None
        self.filename = filename

    def _filename_pre_data(self) -> dict:
        """prepare filename to dict
        pseudo code:
        -get key word form file draft and store it in key
        -split filename with "_" so we will got list of student name, id, ex, etc.
        -we will zip it together and store into prework(dict) that keep student data and key word 
        example: {"student_id": "1234567890", "name": "Alex", "ex": "ex1}
        Returns:
            dict: student data form file name
        """
        key = []
        remainder = ""
        prework = {}
        for i in self.draft_file:
            if i == "{":
                remainder = ""
            elif i == "}":
                key.append(remainder)
            else:
                remainder += i
        list_filename = self.filename.split("_")
        for key, value in zip(key, list_filename):
            prework[key] = value
        self.pre_data = prework

    def prepare_student_data(self) -> dict:
        """make that studect_data(dict) ready for the next step by get the output draft 
        and set it into student_data and have its value is "N/"A
        Returns:
            dict: empty student data that have only data from file name but another is "N/A"
        """
        self._filename_pre_data()
        empty_student = {}
        for i in self.draft_out:
            empty_student[i] = "N/A"
        for i in self.pre_data:
            empty_student[i] = self.pre_data[i]
        self.pre_data = empty_student

    def data_input(self, post_student_data: dict) -> dict:
        """get data form user and set into student data(dict)
        pseudo code:
        for loop post_student_data and if its "N/A" ask user for information
        and store it. But if the input was -99 it will skip that question to next one
        and when its finish it will return post_student_data
        example:
        {'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '10', 'score2': '20', 'comment': 'nice work'}
        Args:
            post_student_data (dict): empty_student_data
        Returns:
            dict: student data that ready to write
        """
        for i in post_student_data:
            if post_student_data[i] == "N/A":
                data_input = inask(f"Enter {i}: ")
                if data_input == "-99":
                    continue
                post_student_data[i] = data_input
        return post_student_data

    def ask(self) -> data_input:
        """ask user for student data
        pseudo code:
        loop empty_student_data if its not "N/A" it will print out its key and value
        then it will call data_input
        Returns:
            data_input: return student data that ready to write
        """
        print("===========================")
        post_student_data = self.pre_data
        for i in post_student_data:
            if post_student_data[i] != "N/A":
                print(f"{i}: {post_student_data[i]}")
        print("===========================")
        post_data = self.data_input(post_student_data)
        return post_data
