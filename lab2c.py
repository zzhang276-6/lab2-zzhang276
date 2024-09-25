#!/usr/bin/env python3

#name = 'Jon'
#age = 20
#print('Hi ' + name + ', you are ' + str(age) + ' years old.')


import sys

if len(sys.argv) != 3:
    print(f"please enter: {sys.argv[0]} name age")
    sys.exit()

name = sys.argv[1]
age = int(sys.argv[2])

print('Hi ' + name + ', you are ' + str(age) + ' years old.')

