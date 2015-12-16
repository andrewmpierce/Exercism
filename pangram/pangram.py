# -*- coding: utf-8 -*-

def is_pangram(string):
    string_list = list(string.lower())
    used_letters = []
    for x in string_list:
        if x.isalpha():
            used_letters.append(x)
    used_letters = set(used_letters)
    if len(used_letters) >= 26:
        return True
    else:
        return False
