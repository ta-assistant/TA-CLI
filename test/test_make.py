from src.build.make import init_work_directory
from lib.file_management import save, readapikey, exsitapikey, removeapikey, readapikey
import unittest
from unittest.mock import patch
import os, inspect, shutil

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


class TestInitWorkDir(unittest.TestCase):
    def setUp(self) -> None:
        self.old_apikey_state = False
        return super().setUp()
        
    @patch('builtins.input',return_value='y')
    def create_env(self,input):
        if exsitapikey():
            self.old_apikey_state = True
            self.old_apikey = readapikey()
        self.assertIsNone(save("testKey"))
        os.mkdir(os.path.join(currentdir,"work_dir"))
        self.work_dir = os.path.join(currentdir,"work_dir")
        print(readapikey())

    
    def test_init_work_dir(self):
        self.create_env()
        self.assertTrue(init_work_directory(self.work_dir,'testWork2'))

    def test_init_work_dir_invalid_workid(self):
        self.create_env()
        self.assertFalse(init_work_directory(self.work_dir,'testWork'))



    @patch('builtins.input',return_value='y')
    def tearDown(self,input) -> None:
        if self.old_apikey_state:
            self.assertIsNone(save(self.old_apikey))
        else:
            removeapikey()
        if os.path.exists(os.path.join(currentdir,"work_dir")):
            shutil.rmtree(os.path.join(currentdir,"work_dir"))
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()