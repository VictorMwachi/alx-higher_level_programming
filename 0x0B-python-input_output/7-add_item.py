#!/usr/bin/python3
"""
module contains script that adds all arguments to 
a Python list, and then save them to a file
"""


import sys.argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


print("enter arguments seperated by space", sys.argv[0])
temp=[]
for i in range(1:len(sys.argv)):
        temp.append(sys.argv[i])
save_to_json("add_item.json",temp)
load_from_json("add_item.json")
