#!/usr/bin/python3
def text_indentation(text):
    after = None
    cha = [':', '.', '?']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(0, len(text)):
        if text[i] in cha:
            print(text[i] + "\n")
            after = True
        else:
            if after is True:
                if text[i] == ' ':
                    if text[i+1] != ' ':
                        after = False
                else:
                    print(text[i], end="") 
