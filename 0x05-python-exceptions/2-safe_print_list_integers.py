#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for n in range x:
            if isinstance(my_list[n], int):
                print(my_list[n])
    except:
