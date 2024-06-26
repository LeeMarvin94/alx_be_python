#!/usr/bin/python3
#python script related to the ALX BE program

number = int(input('Enter a number to see its multiplication table: '))

for i in range(1, 11):
    print(f'{number} * {i} = {number * i}')
