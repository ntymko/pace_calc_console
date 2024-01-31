from utils import PaceCalculator
from converts import *
from texts_of_messages import *
from validator import *


name = input(MES_INPUT_HELLO)
while not name_validator(name):
    name = input(MES_INPUT_HELLO)

answer_1 = input(name + MES_QUES_1)
while not kind_validator(answer_1):
    answer_1 = input(name + MES_QUES_1)

s = input(MES_INPUT_DISTANCE)
while not distance_validator(s):
    s = input(MES_INPUT_DISTANCE)
s = int(s)

if answer_1.lower() == 'темп':
    temp = input(MES_QUES_5)
    while not pace_validator(temp):
        temp = input(name + MES_QUES_1)
    temp_sec = temp_str_to_int_sec(temp)
    calculator_1 = PaceCalculator(s)
    res = get_formating_time_by_seconds(calculator_1.calc_time(temp_sec))
    print(MES_FINAL_1, s, 'метров:', res)
    print(MES_FINAL_2, round(calculator_1.calc_speed(temp_sec), 2), 'км/ч')


elif answer_1.lower() == 'время':
    t = input(MES_QUES_2)
    while not time_validator(t):
        t = input(MES_QUES_2)
    t_sec = time_str_to_int_sec(t)
    calculator = PaceCalculator(s)
    res = get_formating_time_by_seconds(calculator.calc_temp(t_sec))
    print(TEMP, res)
    temp_sec = temp_str_to_int_sec(res)
    print(MES_FINAL_2, round(calculator.calc_speed(temp_sec), 2), 'км/ч')



elif answer_1.lower() == 'скорость':
    u = input(MES_QUES_7)
    while not speed_validator(u):
        u = input(MES_QUES_7)
    u_float = get_str_to_float_speed(u)
    calculator_1 = PaceCalculator(s)
    temp = calculator_1.from_speed_calc_temp(u_float)
    time = calculator_1.calc_time(temp)


    print('Ваше итоговое время:', get_formating_time_by_seconds(time))
    print('Ваш темп:', get_formating_time_by_seconds(temp))



