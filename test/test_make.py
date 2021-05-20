import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.chdir(parentdir+r"\src\build")
sys.path.insert(0,os.getcwd())

import make
from unittest.mock import patch

class TestMake(unittest.TestCase):
    @patch("make.create_draft",return_value='yes')
    def test_init_make(self,input):
        self.assertTrue(make.init_work_directory(currentdir))
        self.assertFalse(make.init_work_directory(currentdir))

    def tearDown(self) -> None:
        make.reset(currentdir)
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()