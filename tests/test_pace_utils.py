import unittest

from utils import Calculator, CalculatorError


class TestCalculator(unittest.TestCase):
    def test_init_calculator(self):
        calc = Calculator(5000)
        self.assertEqual(5000, calc.distance)

        with self.assertRaises(CalculatorError):        #Чтобы "поймать" ошибку, используем with self.assertRaises.....
            calc = Calculator('ddd')

    def test_calc_temp(self):
        calc = Calculator(5000)
        time = 25 * 60 # 25:00
        temp = calc.calc_temp(time)
        self.assertEqual('05:00', temp)

    def test_calc_time(self):
        calc = Calculator(5000)
        temp_sec = 4 * 60   #'04:00'
        time = calc.calc_time(temp_sec)
        self.assertEqual('20:00', time)

    def test_calc_speed(self):
        calc = Calculator(5000)
        temp_sec = 4 * 60  # '04:00'
        u = calc.calc_speed(temp_sec)
        self.assertEqual(15.0, u)

