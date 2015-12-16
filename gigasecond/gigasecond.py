import datetime as dt

def add_gigasecond(birthday):
    td = dt.timedelta(seconds = 1000000000)
    ret = td + birthday
    return ret
