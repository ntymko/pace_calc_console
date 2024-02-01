from utils import *
from converts import *
from texts_of_messages import *
from validator import *


name = input(MES_HELLO)
while not name_validator(name):
    name = input(MES_HELLO)

str_kind = input(name + MES_QUES_KIND)
kind = parse_kind(str_kind)
while kind is None:
    str_kind = input(name + MES_QUES_KIND)

s = input(MES_DISTANCE)
while not distance_validator(s):
    s = input(MES_DISTANCE)
s = int(s)

if kind == Kind.TEMP:
    temp = input(MES_QUES_TEMP)
    while not pace_validator(temp):
        temp = input(name + MES_QUES_KIND)
    temp_sec = temp_str_to_int_sec(temp)
    calculator_1 = PaceCalculator(s)
    res = get_formating_time_by_seconds(calculator_1.calc_time(temp_sec))
    print(MES_FINAL_TIME, s, 'метров:', res)
    print(MES_FINAL_SPEED, round(calculator_1.calc_speed(temp_sec), 2), 'км/ч')


elif kind == Kind.TIME:
    t = input(MES_QUES_TIME)
    while not time_validator(t):
        t = input(MES_QUES_TIME)
    t_sec = time_str_to_int_sec(t)
    calculator = PaceCalculator(s)
    res = get_formating_time_by_seconds(calculator.calc_temp(t_sec))
    print(MES_FINAL_TEMP, res)
    temp_sec = temp_str_to_int_sec(res)
    print(MES_FINAL_SPEED, round(calculator.calc_speed(temp_sec), 2), 'км/ч')


elif kind == Kind.SPEED:
    u = input(MES_QUES_SPEED)
    while not speed_validator(u):
        u = input(MES_QUES_SPEED)
    u_float = get_str_to_float_speed(u)
    calculator_1 = PaceCalculator(s)
    temp = calculator_1.from_speed_calc_temp(u_float)
    time = calculator_1.calc_time(temp)


    print('Ваше итоговое время:', get_formating_time_by_seconds(time))
    print('Ваш темп:', get_formating_time_by_seconds(temp))



