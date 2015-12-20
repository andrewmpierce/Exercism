

def encode(string):
    pass

def decode(string):
    string = list(string)
    ret = []
    for x in string:
        if x.isalpha() and not string[(string.index(x)-1)].isdigit():
            ret.append(x)
        elif x.isalpha() and string[(string.index(x)-1)].isdigit():
            for y in range(int(string[(string.index(x)-1)])):
                ret.append(x)
    ret = ''.join(ret)
    return ret
