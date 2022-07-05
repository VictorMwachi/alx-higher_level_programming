#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if my_string[ch] != 'c' or my_string[ch] != 'C':
            new_string += my_string[ch]
    return new_string
