#
# Skeleton file for the Python "Bob" exercise.
#

def is_question(what):
    what = what.strip()
    if len(what) > 0 and what[-1] == '?':
        return True
    else:
        return False


def is_shout(what):
    what = what.strip()
    letters = 0
    for x in list(what):
        if x == x.upper():
            if x.isalpha():
                letters += 1
            continue
        else:
            return False
    if letters == 0 or len(what) == 0:
        return False
    else:
        return True


def is_ignore(what):
    what = what.strip()
    if len(what) == 0:
        return True
    else:
        return False


def hey(what):
    if is_shout(what):
        return 'Whoa, chill out!'
    elif is_ignore(what):
        return 'Fine. Be that way!'
    elif is_question(what):
        return 'Sure.'
    else:
        return 'Whatever.'
