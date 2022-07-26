#!/usr/bin/python3
def print_square(size):
  """returns a square print in #"""
  
  if type(size) != int:
    raise TypeError("size must be an integer")
  if type(size) is float and size < 0:
    raise TypeError("size must be an integer")
  if size < 0:
    raise ValueError("size must be >= 0")
  for r in range(0, size):
    print('#' * size)
