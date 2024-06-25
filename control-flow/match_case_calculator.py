#!/usr/bin/python3
#python script related to the ALX SE backend program

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

match operation:
    case '+':
        print(f'The result is: {num1 + num2}')
    case '-':
        print(f'The result is: {num1 - num2}')
    case '*':
        print(f'The result is: {num1 * num2}')
    case '/':
        print(f'The result is: {num1 / num2}')
