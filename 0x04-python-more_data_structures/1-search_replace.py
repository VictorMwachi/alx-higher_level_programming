#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = []
    for s in range(len(my_list)):
        if my_list[s] == search:
            my_new_list.append(replace)
        else:
            my_new_list.append(my_list[s])
    return my_new_list
