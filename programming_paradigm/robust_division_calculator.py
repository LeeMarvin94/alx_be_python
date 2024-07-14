#!/usr/bin/python3
# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert arguments to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division and handle ZeroDivisionError
        result = num / den
        return f"The result of {num} divided by {den} is {result}."
        
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
        
    except ValueError:
        return "Error: Both inputs must be numeric values."

# Example usage (comment out before using in main.py):
# if __name__ == "__main__":
#     print(safe_divide(10, 2))
#     print(safe_divide(10, 0))
#     print(safe_divide('a', 2))


