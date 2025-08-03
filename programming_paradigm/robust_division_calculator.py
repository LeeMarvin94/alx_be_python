#!/usr/bin/python3
#ALX python script for learning purposes

def safe_divide(numerator, denominator):
    """Handle division by zero"""
    try:
        #result = float(numerator)/float(denominator)
        result = int(numerator)/int(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        return f"The result of the division is {result}"
    