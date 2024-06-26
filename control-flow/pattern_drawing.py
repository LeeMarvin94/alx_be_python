#!/usr/bin/python3
#python script related to the ALX backend program

size = int(input('Enter the size of the pattern: '))
count = 0
while count < size:
    for i in range(size):
        print('*', end='')
    print('')
    count = count + 1


