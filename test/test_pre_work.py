import unittest
from src.main.pre_work import Work

class TestPreWork(unittest.TestCase):
    def test_assign_variable_all_passed(self):
        work = Work()
        work.workId = 123456 

work = Work()
work.workId = 123456
print(work.workId)