#!/usr/bin/python3
def text_indentation(text):
  cha=[':','.','?']
  if type(text) is not str:
    raise TypeError("text must be a string")
    for ch in text:
      if ch in cha:
        print()
      else:
        print(ch,end="") 
