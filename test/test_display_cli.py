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

        
class TestDisplayApiStatusMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.success_api_message = {"statusCode":200,"message":"Success","requestId":"xxxxxxxxxxx-xxx","workDraft":{"Draft":"draft"}}
        self.fail_api_message = {"statusCode":400,"message":"The workId you specified was not found.","requestId":"xxxxxxxxxxx-xxx","workDraft":{"Draft":"draft"}}
        return super().setUp()

    def _get_io_status_code_200_order(self,order):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_api_status_message(self.success_api_message,order)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()
    
    def _get_io_status_code_200_end(self,end):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_api_status_message(self.success_api_message,1,end)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def _get_io_status_code_fail_order(self,order):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_api_status_message(self.fail_api_message,order,False)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def _get_io_status_code_fail_end(self,end):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_api_status_message(self.fail_api_message,1,end)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def test_status_code_200_order(self):
        expectAnswer1 = """ ├─ [/] statusCode:200
 ├─ [/] message:Success
 ├─ [/] requestId:xxxxxxxxxxx-xxx
"""     
        expectAnswer2 = """[/] statusCode:200
[/] message:Success
[/] requestId:xxxxxxxxxxx-xxx
"""     
        self.assertEqual(self._get_io_status_code_200_order(1),expectAnswer1)
        self.assertEqual(self._get_io_status_code_200_order(0),expectAnswer2)

    def test_status_code_200_end(self):
        expectAnswer1 = """ ├─ [/] statusCode:200
 ├─ [/] message:Success
 ├─ [/] requestId:xxxxxxxxxxx-xxx
"""
        expectAnswer2 = """ ├─ [/] statusCode:200
 ├─ [/] message:Success
 └─ [/] requestId:xxxxxxxxxxx-xxx
"""
        self.assertEqual(self._get_io_status_code_200_end(False),expectAnswer1)
        self.assertEqual(self._get_io_status_code_200_end(True),expectAnswer2)

    def test_status_code_fail_order(self):
        expectAnswer1 = """ ├─ [x] statusCode:400
 ├─ [x] message:The workId you specified was not found.
 ├─ [x] requestId:xxxxxxxxxxx-xxx
"""     
        expectAnswer2 = """[x] statusCode:400
[x] message:The workId you specified was not found.
[x] requestId:xxxxxxxxxxx-xxx
"""     
        self.assertEqual(self._get_io_status_code_fail_order(1),expectAnswer1)
        self.assertEqual(self._get_io_status_code_fail_order(0),expectAnswer2)

    def test_status_code_fail_end(self):
        expectAnswer1 = """ ├─ [x] statusCode:400
 ├─ [x] message:The workId you specified was not found.
 ├─ [x] requestId:xxxxxxxxxxx-xxx
"""
        expectAnswer2 = """ ├─ [x] statusCode:400
 ├─ [x] message:The workId you specified was not found.
 └─ [x] requestId:xxxxxxxxxxx-xxx
"""
        self.assertEqual(self._get_io_status_code_fail_end(False),expectAnswer1)
        self.assertEqual(self._get_io_status_code_fail_end(True),expectAnswer2)


class TestDisplayConfiguration(unittest.TestCase):
    def setUp(self) -> None:
        # length of self.draft is 126
        self.even_draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comments', 'score', 'scoreTimestamp']}
        # length of self.draft is 125
        self.odd_draft = {"fileDraft": "{studentId}_test.zip","outputDraft": ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp']}
        self.workId = 123456
        self.ta_api = "https://ta-api.testserver.com/"
        self.number_file = 50
        return super().setUp()
    
    def _get_io_configuration_odd(self):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_configuration(self.odd_draft,self.workId,self.ta_api,self.number_file)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def _get_io_configuration_even(self):
        # create StringIO object
        capturedOutput = io.StringIO()
        # Redirect stdout
        sys.stdout = capturedOutput
        # call function
        display_configuration(self.even_draft,self.workId,self.ta_api,self.number_file)
        # reset redirect.
        sys.stdout = sys.__stdout__
        return capturedOutput.getvalue()

    def test_longest_is_odd(self):
        expectAnswer = """+--------------------------------------------------------------------------------------------+
|                                      [ Configuration ]                                     |
+--------------------------------------------------------------------------------------------+
|      ta-api      |                      https://ta-api.testserver.com/                     |
+--------------------------------------------------------------------------------------------+
|      workId      |                                  123456                                 |
+--------------------------------------------------------------------------------------------+
|    fileDraft     |                           {studentId}_test.zip                          |
+--------------------------------------------------------------------------------------------+
|   outputDraft    | ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp'] |
+--------------------------------------------------------------------------------------------+
| Number of files  |                                    50                                   |
+--------------------------------------------------------------------------------------------+
"""
        self.assertEqual(self._get_io_configuration_odd(),expectAnswer)
    
    def test_longest_is_even(self):
        expectAnswer = """+---------------------------------------------------------------------------------------------+
|                                      [ Configuration ]                                      |
+---------------------------------------------------------------------------------------------+
|      ta-api      |                      https://ta-api.testserver.com/                      |
+---------------------------------------------------------------------------------------------+
|      workId      |                                  123456                                  |
+---------------------------------------------------------------------------------------------+
|    fileDraft     |                           {studentId}_test.zip                           |
+---------------------------------------------------------------------------------------------+
|   outputDraft    | ['studentId', 'param1', 'param2', 'comments', 'score', 'scoreTimestamp'] |
+---------------------------------------------------------------------------------------------+
| Number of files  |                                    50                                    |
+---------------------------------------------------------------------------------------------+
"""
        self.assertEqual(self._get_io_configuration_even(),expectAnswer)

if __name__ == "__main__":
    unittest.main()