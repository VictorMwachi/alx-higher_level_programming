#!/usr/bin/python3
def safe_print_list(my_list = [], x = 0):
    try:
        for i in range(x):
            if i < x:
                print("{}".format(my_list[i]), end="")
            else:
                print()          
    except IndexError:
        print()
