import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from lib.file_management.function_network.func_network import CallApi

class TestCallApi(unittest.TestCase):
    def setUp(self) -> None:
        self.call = CallApi('K4nPEs7RhhCzcjdlvr3X==', 'testWork2', parentdir+r'\testypath')
        return super().setUp()

    def test_readprefix(self):
        """
        return str

        """
        self.assertEqual(self.call.readprefix(), 'https://ta-api.sirateek.dev/')

    def TestCreateWork(self):
        """
        print(str)
        """
        self.assertEqual(self.call.createworkdraft(), 'Success to access')

    def TestWritejson(self):
        """
        print(str)
        """
        self.assertEqual(self.call.writejson(), 'Sending data success')



if __name__ == "__main__":
    unittest.main()