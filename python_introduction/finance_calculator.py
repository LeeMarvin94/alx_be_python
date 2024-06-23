#!/usr/bin/python3

income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))
Monthly_savings = income - expenses
print(f'Your monthly savings are ${Monthly_savings}')
Projected_savings = int(Monthly_savings * 12 + (Monthly_savings * 12 * 0.05))
print(f'Projected savings after one year, with interest, is: ${Projected_savings}')


#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
