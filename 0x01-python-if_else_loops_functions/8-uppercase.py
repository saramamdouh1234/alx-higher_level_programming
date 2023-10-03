#!/usr/bin/python3
def uppercase(ptr):
    for c in ptr:
        temp = ord(c)
        if temp >= 97 and temp <= 122:
            temp -= 32
        print("{:c}".format(temp), end='')
    print()
