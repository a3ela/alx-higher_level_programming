#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = 0
    for i in my_list:
        if maxNum < i:
            maxNum = i
    
    return maxNum
