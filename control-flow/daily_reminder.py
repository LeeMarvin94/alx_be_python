#!/usr/bin/python3
#python script related to the ALX SE program

Task = input('Enter your task: ')
Priority = input('Priority (high/medium/low): ')
TimeBount = input('Is is time-bound? (yes/no): ')

if timeBount == 'yes':
    match priority:
        case 'high':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
        case 'medium':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
        case 'low':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")

