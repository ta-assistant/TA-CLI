from lib.file_management.createapikeyfile import SaveApiKey
from src.build.make import init_work_directory, reset
import json
import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)


class TestMake(unittest.TestCase):
    def test_init_make(self):
        """
        call init_work_directory to set test to work dir
        Args:
            input (str): "yes"
        """
        SaveApiKey().save('K4nPEs7RhhCzcjdlvr3X==')
        self.assertIsNone(init_work_directory(currentdir, 'testWork2'))

    def tearDown(self) -> None:
        """
        when test finish reset test into normal dir (not work directory)
        """
        reset(currentdir)
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
