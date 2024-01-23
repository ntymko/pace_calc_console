import unittest
from validator import *

class TestValidators(unittest.TestCase):

    def test_pace_validator(self):
        temp = pace_validator('7:59')
        self.assertEqual(True, temp)

        temp = pace_validator('7:61')
        self.assertEqual(False, temp)

    def test_time_validator(self):
        t = time_validator('25:45')
        self.assertEqual(True, t)

        t = time_validator('25:78')
        self.assertEqual(False, t)

        t = time_validator('dfxgchvjbnkm')
        self.assertEqual(False, t)

    def test_date_validator(self):
        date = date_validator('темп')
        self.assertEqual(True, date)

        date = date_validator('Темп')
        self.assertEqual(True, date)

        date = date_validator('ТЕМП')
        self.assertEqual(True, date)

        date = date_validator('ewfzxrthcfvyjukbnlio;mp')
        self.assertEqual(False, date)

        date = date_validator('7846512354')
        self.assertEqual(False, date)

    def test_distance_validator(self):
        distance = distance_validator('5000')
        self.assertEqual(True, distance)

        distance = distance_validator('Ezwrxtchyvubi')
        self.assertEqual(False, distance)

        distance = distance_validator('-!!!!!!!rtdfy')
        self.assertEqual(False, distance)

    def test_name_validator(self):
        name = name_validator('Наталья')
        self.assertEqual(True, name)

        name = name_validator('456312.')
        self.assertEqual(False, name)

        name = name_validator('Natalia_Tymko')
        self.assertEqual(True, name)

        name = name_validator('Natalia Tymko')
        self.assertEqual(True, name)








