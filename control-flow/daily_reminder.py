#!/usr/bin/python3
#python script related to the ALX SE program

task = input('Enter your task: ')
priority = input('Priority (high/medium/low): ')
time_bound = input('Is is time-bound? (yes/no): ')

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today")
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time")
