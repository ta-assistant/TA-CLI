from src.build.make import init_work_directory
from src.main.run_work import run_work
from lib.file_management import save_api_key, readapikey, exsitapikey, removeapikey, readapikey
import unittest
import zipfile, json
from unittest.mock import patch
import os, inspect, shutil

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

class TestRunWork(unittest.TestCase):
    def setUp(self) -> None:
        self.old_apikey_state = False
        self.work_dir = os.path.join(currentdir,"work_dir")
        os.mkdir(self.work_dir)
        self.create_env("testKey")
        init_work_directory(self.work_dir,"testWork2")
        return super().setUp()

    def create_file_zip(self,name):
        listname = ["test_1.txt","test_2.txt","test_3.txt"]
        test_data = "123456"
        # Create test file
        for filename in listname:
            with open(os.path.join(self.work_dir,filename),"w") as file:
                json.dump(test_data,file)
                file.close()
        self.path_target = os.path.join(self.work_dir,f"{name}.zip")
        with zipfile.ZipFile(self.path_target,"w") as my_zip:
            text_1 = os.path.join(self.work_dir,"test_1.txt")
            text_2 = os.path.join(self.work_dir,"test_2.txt")
            text_3 = os.path.join(self.work_dir,"test_3.txt")
            my_zip.write(text_1,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_2,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.write(text_3,compress_type=zipfile.ZIP_DEFLATED)
            my_zip.close()

    @patch('builtins.input',return_value='y')
    def create_env(self,apikey,input):
        if exsitapikey():
            self.old_apikey_state = True
            self.old_apikey = readapikey()
        self.assertIsNone(save_api_key(apikey))

    @patch('builtins.input',side_effect=["r"])
    def test_no_file_to_run(self,input):
        self.assertFalse(run_work(self.work_dir,False,False))

    side_effect = [1 for _ in range(20)]
    @patch('builtins.input',side_effect=['r']+side_effect)
    def test_run_work_read(self,input):
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertTrue(run_work(self.work_dir,False,False))

    side_effect = [1 for _ in range(20)]
    @patch('builtins.input',side_effect=['f']+side_effect)
    def test_no_draft_choose_fetch(self,input):
        os.remove(os.path.join(self.work_dir,"ta","draft.json"))
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertTrue(run_work(self.work_dir,False,False))

    side_effect = [1 for _ in range(20)]
    @patch('builtins.input',side_effect=['r']+side_effect)
    def test_no_draft_choose_read(self,input):
        os.remove(os.path.join(self.work_dir,"ta","draft.json"))
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertFalse(run_work(self.work_dir,False,False))

    side_effect = [1 for _ in range(20)]
    @patch('builtins.input',side_effect=['f']+side_effect)
    def test_run_work_fetch(self,input):
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertTrue(run_work(self.work_dir,False,False))
    
    side_effect = [str(-99) for _ in range(20)]
    @patch('builtins.input',side_effect=['f']+side_effect)
    def test_run_work_pass_input(self,input):
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertTrue(run_work(self.work_dir,False,False))

    @patch('builtins.input',side_effect=['r'])
    def test_run_work_no_draft(self,input):
        os.remove(os.path.join(self.work_dir, "ta", "draft.json"))
        self.assertFalse(run_work(self.work_dir,False,False))
    
    @patch('builtins.input',side_effect=['r'])
    def test_run_work_no_config(self,input):
        os.remove(os.path.join(self.work_dir, "ta", "config.json"))
        self.assertFalse(run_work(self.work_dir,False,False))

    @patch('builtins.input',side_effect=['f'])
    def test_run_work_fetch_but_no_apikey(self,input):
        removeapikey()
        self.assertFalse(run_work(self.work_dir,False,False))
    
    @patch('builtins.input',side_effect=['r'])
    def test_run_work_read_but_no_apikey(self,input):
        removeapikey()
        self.create_file_zip("6310546066")
        self.create_file_zip("6310546065")
        self.create_file_zip("6310546064")
        self.create_file_zip("6310546063")
        self.create_file_zip("6310546062")
        self.assertTrue(run_work(self.work_dir,False,False))

    @patch('builtins.input',side_effect=['r'])
    def test_no_file_follow_draft(self,input):
        listname = ["test_1.txt","test_2.txt","test_3.txt"]
        test_data = "123456"
        # Create test file
        for filename in listname:
            with open(os.path.join(self.work_dir,filename),"w") as file:
                json.dump(test_data,file)
                file.close()
        self.assertFalse(run_work(self.work_dir,False,False))

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