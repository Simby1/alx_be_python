task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Try to complete it as soon as possible."
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " that should be completed today."
        else:
            reminder += ". You should work on it soon."
    case 'low':
        reminder = f"'{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += ". It is time-bound, so try to finish it today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = f"'{task}' has an unknown priority."

print(f"\nReminder: {reminder}")
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")