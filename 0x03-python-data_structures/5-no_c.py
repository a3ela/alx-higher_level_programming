#!/usr/bin/python3
def no_c(my_string):
    newString = ''
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            pass
        else:
            newString += letter
    
    return newString
