from src.build.make import init_work_directory
from lib.file_management import save_api_key, readapikey, exsitapikey, removeapikey, readapikey
import unittest
from unittest.mock import patch
import os, inspect, shutil

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


class TestInitWorkDir(unittest.TestCase):
    def setUp(self) -> None:
        self.old_apikey_state = False
        self.work_dir = os.path.join(currentdir,"work_dir")
        os.mkdir(self.work_dir)
        return super().setUp()
        
    @patch('builtins.input',return_value='y')
    def create_env(self,apikey,input):
        if exsitapikey():
            self.old_apikey_state = True
            self.old_apikey = readapikey()
        self.assertIsNone(save_api_key(apikey))
    def rm_apikey(self):
        if exsitapikey():
            self.old_apikey_state = True
            self.old_apikey = readapikey()
            removeapikey()
    def check_file(self):
        # all success can create config and fetch draft
        self.sucess = os.path.exists(os.path.join(currentdir,"work_dir","ta")) and \
            os.path.exists(os.path.join(currentdir,"work_dir","ta","config.json")) and os.path.exists(os.path.join(currentdir,"work_dir","ta","draft.json"))
        # cannot fetch draft
        self.cant_fetch_draft = os.path.exists(os.path.join(currentdir,"work_dir","ta")) and \
            os.path.exists(os.path.join(currentdir,"work_dir","ta","config.json")) and not os.path.exists(os.path.join(currentdir,"work_dir","ta","draft.json"))


    def test_init_work_dir(self):
        # all good
        self.create_env("testKey")
        self.assertTrue(init_work_directory(self.work_dir,'testWork2'))
        self.check_file()
        self.assertTrue(self.sucess)
        self.assertFalse(self.cant_fetch_draft)
        
    def test_init_work_dir_invalid_workid(self):
        self.create_env("testKey")
        # wrong work id
        self.assertFalse(init_work_directory(self.work_dir,'testWork'))
        self.check_file()
        self.assertFalse(self.sucess)
        self.assertTrue(self.cant_fetch_draft)

    def test_init_work_dir_invalid_apikey(self):
        # wrong api-key
        self.create_env("testKey1")
        self.assertFalse(init_work_directory(self.work_dir,'testWork2'))
        self.check_file()
        self.assertFalse(self.sucess)
        self.assertTrue(self.cant_fetch_draft)

    def test_init_work_dir_not_have_apikey(self):
        # not have api-key
        self.rm_apikey()
        self.assertFalse(init_work_directory(self.work_dir,'testWork2'))
        self.check_file()
        self.assertFalse(self.sucess)
        self.assertTrue(self.cant_fetch_draft)

    @patch('builtins.input',return_value='y')
    def tearDown(self,input) -> None:
        if self.old_apikey_state:
            self.assertIsNone(save_api_key(self.old_apikey))
        else:
            removeapikey()
        if os.path.exists(os.path.join(currentdir,"work_dir")):
            shutil.rmtree(os.path.join(currentdir,"work_dir"))
        return super().tearDown()

if __name__ == "__main__":
    unittest.main()