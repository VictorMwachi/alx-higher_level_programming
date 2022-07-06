#!/usr/bin/python3
def search_replace(my_list, search, replace):
  for s in range(len(my_list)-1):
    if my_list[s] == search:
    my_list[s] = replace
  return my_list
