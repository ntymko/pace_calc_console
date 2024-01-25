class Calculator:
    def __init__(self, distance):
        if type(distance) != int:
            raise CalculatorError('Неверный тип дистанции')

        self.distance = int(distance)

    def calc_temp(self, time_sec):
        '''Для расчета темпа бега в секундах'''
        u = self.distance / time_sec * 3600 / 1000
        temp = 3600 / u
        return temp

    def calc_time(self, temp_sec):
        '''Для расчета времени в секундах'''
        u = 3600 / temp_sec
        t = int(self.distance) * 3.6 / u
        return t

    def calc_speed(self, temp_sec):
        '''Для рассчета скорости'''
        u = 3600 / temp_sec
        return u



class CalculatorError(Exception):
    pass