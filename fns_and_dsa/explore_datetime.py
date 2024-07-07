from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the current date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future date: {formatted_future_date}")
    return future_date

if __name__ == "__main__":
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(current_date, days_to_add)

