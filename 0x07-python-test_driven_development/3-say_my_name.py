#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
  """returns concat of first and last name with space in between"""
  
  if type(first_name) is not string:
    raise TypeError("first_name must be a string")
  if type(last_name) is not string:
    raise TypeError("last_name must be a string"
  return "My name is "first name + " " + last name
