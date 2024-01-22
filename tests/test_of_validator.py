import unittest
from validator import *

class TestConvers(unittest.TestCase):

    def test_pace_validator(self):
        temp = pace_validator('7:59')
        self.assertEqual(True, temp)

        temp = pace_validator('7:61')
        self.assertEqual(False, temp)





