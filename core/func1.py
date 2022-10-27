import time


def get_time():
    """ 
    返回年月时分秒
    return 2022,09,04,21,13,31
    """
    return time.strftime('%Y'), time.strftime('%m'), time.strftime('%d'), time.strftime('%H'), time.strftime('%M'), time.strftime('%S')

def get_nian():
    """ 
    返回年
    return 2022
    """
    return time.strftime('%Y')

def get_yue():
    """ 
    返回月
    return 09
    """
    return time.strftime('%m')

def get_ri():
    """ 
    返回日
    return 04
    """
    return time.strftime('%d')


