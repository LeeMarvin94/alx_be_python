class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(5, 3)
    print(f"The sum of 5 and 3 is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(4, 6)
    print(f"The product of 4 and 6 is: {product_result}")

