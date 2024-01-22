import unittest

from converts import t_transform, temp_transform

class TestConvers(unittest.TestCase):

    def test_t_transform(self):
        time = '15:27'
        t_sec = t_transform(time)
        self.assertEqual(927, t_sec)


    def test_temp_transform(self):
        temp = '7:50'
        temp_sec = temp_transform(temp)
        self.assertEqual(470, temp_sec)




