import unittest
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
print(parentdir)
from lib.file_management.function_network.func_network import SendData

class TestSendData(unittest.TestCase):
    def setUp(self) -> None:
        self.post = SendData('K4nPEs7RhhCzcjdlvr3X==', 'testWork2', parentdir+r'\testypath')
        return super().setUp()

    def testgetworkdraft(self):
        """
        return None
        """
        self.assertIsNone(self.post.getworkDraft(), 'Sending data success')



if __name__ == '__main__':
    unittest.main()