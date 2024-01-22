from utils import Calculator
from converts import *
from texts_of_messages import *
from validator import *  # *- значит, импортировать всЁ из файла


name = input(MES_INPUT_HELLO)
answer_1 = input(name + MES_QUES_1)
while not date_validator(answer_1):
    answer_1 = input(name + MES_QUES_1)

s = input(MES_INPUT_DISTANCE)
while not distance_validator(s):
    s = input(MES_INPUT_DISTANCE)
s = int(s)



if answer_1 == 'темп':
    t = input(MES_QUES_2)
    while not time_validator(t):
        t = input(MES_QUES_2)


    t_sec = t_transform(t)
    obj = Calculator(s)
    res = get_formating_time_by_seconds(obj.calc_temp(t_sec))
    print(TEMP, res)

elif answer_1 == 'время':
    temp = input(MES_QUES_3)
    temp_sec = temp_transform(temp)
    while not pace_validator(temp):
        temp = input(MES_QUES_3)

    obj_1 = Calculator(s)
    res = get_formating_time_by_seconds(obj_1.calc_time(temp_sec))
    print(MES_FINAL_1, s, 'метров:', res)

elif answer_1 == 'скорость':
    temp = input(MES_QUES_3)
    temp_sec = temp_transform(temp)
    while not pace_validator(temp):
        temp = input(MES_QUES_3)

    obj_1 = Calculator(s)
    print(MES_FINAL_2, round(obj_1.calc_speed(temp_sec), 2), 'км/ч')
