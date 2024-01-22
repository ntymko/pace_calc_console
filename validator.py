def distance_validator(distance):                                                  #Проверка валидности дистанции
    try:
        dist = int(distance)
        return True
    except Exception:
        return False



def date_validator(answer_1):                                                       #Проверка 'темп, время, скорость'
    if answer_1.lower() in ('темп', 'скорость', 'время'):
        return True
    else:
        return False

def time_validator(t):                                                              #Проверка валидности времени
    parts = t.split(':')
    length = len(parts)
    if 1 == length or length > 3:
        return False
    for i in parts:
        if not i.isdigit():
            return False
    seconds = int(parts[-1])
    if seconds > 59:
        return False
    else:
        return True

def pace_validator(temp):                                                           #Проверка валидности темпа
    temp_list = temp.split(':')
    if len(temp_list) == 2:
        for i in temp_list:
            if not i.isdigit():
                return False

        seconds = int(temp_list[-1])
        if seconds > 59:
            return False
        else:
            return True
    else:
        return False


