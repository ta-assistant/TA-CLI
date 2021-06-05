import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
<<<<<<< HEAD
os.chdir(parentdir+r"\src\build")
sys.path.insert(0,os.getcwd())

import make
from unittest.mock import patch

class TestMake(unittest.TestCase):
    
    @patch("make.create_draft",return_value='yes')
=======

sys.path.insert(0,parentdir)
import json
from src.build.make import init_work_directory, reset
from lib.file_management.createapikeyfile import SaveApiKey


class TestMake(unittest.TestCase):
<<<<<<< HEAD
    @patch("src.build.make.create_draft",return_value='yes')
>>>>>>> master
    def test_init_make(self,input):
=======
    def test_init_make(self):
>>>>>>> master
        """
        call init_work_directory to set test to work dir
        Args:
            input (str): "yes"
        """
<<<<<<< HEAD
<<<<<<< HEAD
        self.assertTrue(make.init_work_directory(currentdir))
        self.assertFalse(make.init_work_directory(currentdir))
=======
        self.assertTrue(init_work_directory(currentdir))
=======
        SaveApiKey().save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertIsNone(init_work_directory(currentdir,'testWork2'))
>>>>>>> master
        
>>>>>>> master

    def tearDown(self) -> None:
        """
        when test finish reset test into normal dir (not work directory)
        """
<<<<<<< HEAD
        make.reset(currentdir)
=======
        reset(currentdir)
>>>>>>> master
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()