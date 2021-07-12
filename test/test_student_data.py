from src.main.student_data import StudentData
import unittest
from unittest.mock import patch
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)


if __name__ == "__main__":
    unittest.main()
