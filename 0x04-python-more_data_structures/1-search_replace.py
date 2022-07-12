#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = []
    for s in range(len(my_list)-1):
        if my_list[s] == search:
            my_new_list.append(replace)
    return my_new_list
