from utils import Calculator
from converts import t_transform, temp_transform
from texts_of_messages import *
import time

name = input(MES_INPUT_HELLO)
answer_1 = input(name + MES_QUES_1)

if answer_1 == 'темп':
    s = input(MES_INPUT_DISTANCE)
    t = input(MES_QUES_2)
    t_sec = t_transform(t)
    obj = Calculator(s)
    res = time.strftime('%M:%S', time.gmtime(obj.calc_temp(t_sec)))
    print(TEMP, res)

elif answer_1 == 'время':
    s = input(MES_INPUT_DISTANCE)
    temp = input(MES_QUES_3)
    temp_sec = temp_transform(temp)
    obj_1 = Calculator(s)
    res = time.strftime('%M:%S', time.gmtime(obj_1.calc_time(temp_sec)))
    print(MES_FINAL_1, s, 'метров:', res)

elif answer_1 == 'скорость':
    s = input(MES_INPUT_DISTANCE)
    temp = input(MES_QUES_3)
    temp_sec = temp_transform(temp)
    obj_1 = Calculator(s)
    print(MES_FINAL_2, round(obj_1.calc_speed(temp_sec), 2), 'км/ч')
