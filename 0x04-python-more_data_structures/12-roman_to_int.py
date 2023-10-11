#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    j = 0

    if type(roman_string) is str and roman_string:
        for n in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[n]] >= j:
                i += val[roman_string[n]]
            else:
                i -= val[roman_string[n]]
            j = val[roman_string[n]]
    return i
