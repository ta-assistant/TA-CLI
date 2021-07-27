import unittest
import io
import sys

from lib.cli_displayed import *

class TestDisplayStatusSymbol(unittest.TestCase):
    def _get_io_order_test(self,order):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_status_symbol(order,0,"test oreder")
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def _get_io_symbol_test(self,symbol):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_status_symbol(0,symbol,"test symbol")
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def _get_io_order_symbol_test(self,order,symbol):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_status_symbol(order,symbol,"test oreder and symbol")
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def test_display_status_symbol_order(self):
        self.assertEqual(self._get_io_order_test(0),"[/] test oreder\n")
        self.assertEqual(self._get_io_order_test(1)," ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(2)," │   ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(3)," │       ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(4)," │           ├─ [/] test oreder\n")
    
    def test_display_status_symbol_symbol(self):
        self.assertEqual(self._get_io_symbol_test(0),"[/] test symbol\n")
        self.assertEqual(self._get_io_symbol_test(1),"[x] test symbol\n")
        self.assertEqual(self._get_io_symbol_test(2),"[*] test symbol\n")

    def test_display_status_symbol_symbol_and_order(self):
        self.assertEqual(self._get_io_order_symbol_test(0,0),"[/] test oreder and symbol\n")
        self.assertEqual(self._get_io_order_symbol_test(1,1)," ├─ [x] test oreder and symbol\n")
        self.assertEqual(self._get_io_order_symbol_test(2,2)," │   ├─ [*] test oreder and symbol\n")

        


if __name__ == "__main__":
    unittest.main()