#!/usr/bin/python3
def best_score(a_dictionary):
  keys_list = []
  for key in a_dictionary.keys:
    keys_list.append(key)
  return(max(keys_list))
