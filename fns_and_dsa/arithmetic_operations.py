#!/usr/bin/python3
#python script for learning purposes

def perform_operation(num1, num2, operation):
    #'add', 'subtract', 'multiply', or 'divide'
    if operation == 'add':
        return (num1 + num2)
    elif operation == 'subtract':
        return (num1 - num2)
    elif operation == 'multiply':
        return (num1 * num2)
    else:
        if num2 == 0:
            return (0)
        return (num1 / num2)