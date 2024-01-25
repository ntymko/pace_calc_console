from utils import Calculator
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



if answer_1 == 'темп':
    t = input(MES_QUES_2)
    while not time_validator(t):
        t = input(MES_QUES_2)


    t_sec = time_str_to_int_sec(t)
    calculator = Calculator(s)
    res = get_formating_time_by_seconds(calculator.calc_temp(t_sec))
    print(TEMP, res)

elif answer_1 == 'время':
    temp = input(MES_QUES_3)
    temp_sec = temp_str_to_int_sec(temp)
    while not pace_validator(temp):
        temp = input(MES_QUES_3)

    calculator_1 = Calculator(s)
    res = get_formating_time_by_seconds(calculator_1.calc_time(temp_sec))
    print(MES_FINAL_1, s, 'метров:', res)

elif answer_1 == 'скорость':
    temp = input(MES_QUES_3)
    temp_sec = temp_str_to_int_sec(temp)
    while not pace_validator(temp):
        temp = input(MES_QUES_3)

    calculator_1 = Calculator(s)
    print(MES_FINAL_2, round(calculator_1.calc_speed(temp_sec), 2), 'км/ч')
