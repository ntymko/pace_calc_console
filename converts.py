#Методы для конвертации

import time

def t_transform(t):
    t_sek_list = t.split(':')
    t_total = 0
    if len(t_sek_list) == 2:  # МИНУТЫ:СЕКУНДЫ
        first = True
        for i in t_sek_list:
            if first:
                t_total += int(i) * 60
                first = False
            else:
                t_total += int(i)

    if len(t_sek_list) == 3:
        for i in range(len(t_sek_list)):
            if i == 0 or i == 1:
                t_total += int(t_sek_list[i]) * 3600
            else:
                t_total += int(t_sek_list[i])
    return t_total

def temp_transform(Temp):   # '7:50'
    Temp_list = Temp.split(':')
    Temp_sec = int(Temp_list[0]) * 60 + int(Temp_list[1])
    return Temp_sec


def get_formating_time_by_seconds(seconds):
    format = '%M:%S'
    if seconds >= 3600:
        format = '%H:%M:%S'

    return time.strftime(format, time.gmtime(seconds))