#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args = sys.argv
num_args = len(args)

if num_args == 1:
    print('0 arguments.')
else:
    num_args -= 1
    print('{} argument{}:'.format(
        num_args,
        '' if num_args == 1 else 's'))
    for i in range(1, num_args + 1):
        print('{}: {}'.format(i, args[i]))
