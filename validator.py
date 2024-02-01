def name_validator(name):
    '''Для проверки имени на валидность'''
    if name.isalpha() == True:
        return True
    name = name.replace(' ', '_')
    a = name.split('_')
    for i in a:
        if i.isalpha() != True:
            return False
    return True

def distance_validator(distance):
    '''Для проверки валидности дистанции'''
    try:
        dist = int(distance)
        return True
    except Exception:
        return False

def time_validator(t):
    '''Для проверки валидности времени'''
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

def pace_validator(temp):
    '''Для проверки валидности темпа'''
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


def speed_validator(u):
    '''Для проверки валидности скорости'''
    if type(u) != str:
        return False

    if ',' in u:
        u_list = u.split(',')
        for i in u_list:
            if not i.isdigit():
                return False
        return True

    try:
        a = float(u)
    except:
        return False
    return True












