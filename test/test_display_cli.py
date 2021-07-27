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

    def test_display_status_symbol_order(self):
        self.assertEqual(self._get_io_order_test(0),"[/] test oreder\n")
        self.assertEqual(self._get_io_order_test(1)," ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(2)," │   ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(3)," │       ├─ [/] test oreder\n")
        self.assertEqual(self._get_io_order_test(4)," │           ├─ [/] test oreder\n")
        


if __name__ == "__main__":
    unittest.main()