import unittest
from converts import *


class TestConvers(unittest.TestCase):

    def test_time_str_to_int_sec(self):
        time = '15:27'
        t_sec = time_str_to_int_sec(time)
        self.assertEqual(927, t_sec)


    def test_temp_str_to_int_sec(self):
        temp = '7:50'
        temp_sec = temp_str_to_int_sec(temp)
        self.assertEqual(470, temp_sec)


    def test_get_str_to_float_speed(self):
        speed = '7,5'
        speed_new = get_str_to_float_speed(speed)
        self.assertEqual(7.5, speed_new)


