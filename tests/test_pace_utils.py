import unittest
from utils import PaceCalculator, PaceCalculatorError


class TestPaceCalculator(unittest.TestCase):
    def test_init_calculator(self):
        calc = PaceCalculator(5000)
        self.assertEqual(5000, calc.distance)

        with self.assertRaises(PaceCalculatorError):        #Чтобы "поймать" ошибку, используем with self.assertRaises.....
            calc = PaceCalculator('ddd')

    def test_calc_temp(self):
        calc = PaceCalculator(5000)
        time = 25 * 60 # 25:00
        temp = calc.calc_temp(time)
        self.assertEqual(300, temp)

    def test_calc_time(self):
        calc = PaceCalculator(5000)
        temp_sec = 4 * 60   #'04:00'
        time = calc.calc_time(temp_sec)
        self.assertEqual(1200, time)

    def test_calc_speed(self):
        calc = PaceCalculator(5000)
        temp_sec = 4 * 60  # '04:00'
        u = calc.calc_speed(temp_sec)
        self.assertEqual(15.0, u)

