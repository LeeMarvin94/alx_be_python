#!/usr/bin/python3

income = float(input('Enter your monthly income: '))
expenses = float(input('Enter your total monthly expenses: '))
monthlySavings = income - expenses
print(f'Your monthly savings are ${monthlySavings}')
projectedSavings = (monthlySavings * 12) + (monthlySavings * 12 * 0.05)
print(f'Projected savings after one year, with interest, is: ${projectedSavings}')

