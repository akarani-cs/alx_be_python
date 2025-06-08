from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format as YYYY-MM-DD HH:MM:SS
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add: "))  # Get user input
    future_date = datetime.now() + timedelta(days=number_of_days)  # Calculate future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format as YYYY-MM-DD
    print("Future Date:", formatted_future_date)

# Run functions
display_current_datetime()
calculate_future_date()
