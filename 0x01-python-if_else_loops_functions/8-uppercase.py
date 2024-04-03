#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        charNum = ord(str[i])
        if charNum >= 97 and charNum <= 122:
            charNum = ord(str[i]) - 32
        print('{:c}'.format(charNum), end='')
    print()
