# Prompt for task details
task = input("Enter the task description: ")
priority = input("Set the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"⚠️ Urgent Task: {task} - Priority: HIGH"
    case "medium":
        reminder = f"🔶 Important Task: {task} - Priority: MEDIUM"
    case "low":
        reminder = f"✅ Low-Priority Task: {task} - Priority: LOW"
    case _:
        reminder = f"Task: {task} - Priority Unspecified"

# Modify reminder if task is time-sensitive
if time_bound == "yes":
    reminder += " - That requires immediate attention today!"

# Provide customized reminder
print(reminder)
