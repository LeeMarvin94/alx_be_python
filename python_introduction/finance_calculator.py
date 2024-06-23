#!/usr/bin/python3

income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))
monthlySavings = income - expenses
print(f'Your monthly savings are ${monthlySavings}')
projectedSavings = int(monthlySavings * 12 + (monthlySavings * 12 * 0.05))
print(f'Projected savings after one year, with interest, is: ${projectedSavings}')


#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
