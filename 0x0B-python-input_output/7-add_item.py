#!/usr/bin/python3
"""
module contains script that adds all arguments to 
a Python list, and then save them to a file
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


print("enter arguments seperated by space", sys.argv[0])
save_to_json_file(sys.argv[1:],"add_item.json")
load_from_json_file("add_item.json")