import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir+r"\src\build")
sys.path.insert(0,os.getcwd())

import make
import unittest

class TestMake(unittest.TestCase):
    def test_make(self):
        make.init_work_directory(currentdir)
        make.init_work_directory(currentdir)

if __name__ == "__main__":
    unittest.main()