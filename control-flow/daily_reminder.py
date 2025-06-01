# daily_reminder.py

# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Generate customized reminder using match-case and if-statement
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task"
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level"

# Add extra message if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final reminder
print(reminder)
