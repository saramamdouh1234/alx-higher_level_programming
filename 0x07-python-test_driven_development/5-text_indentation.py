#!/usr/bin/python3
"""
This is the text_indentation module.

"""


def text_indentation(text):
    """
    Print a text with 2 new lines 
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for count in range(len(text)):
        line += text[count]
        if text[count] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
