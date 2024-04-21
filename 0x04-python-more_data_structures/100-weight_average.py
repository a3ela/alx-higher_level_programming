#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    leftTotal = 0
    rightTotal = 0

    for tup in my_list:
        leftTotal += tup[0] * tup[1]
        rightTotal += tup[-1]
    return leftTotal/rightTotal
