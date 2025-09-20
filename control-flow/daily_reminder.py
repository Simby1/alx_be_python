task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

match priority:
    case 'high':
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            reminder_message += " that requires immediate attention today!"
            print("Reminder: " + reminder_message)
        else:
            print("Reminder: " + reminder_message)

    case 'medium':
        reminder_message = f"'{task}' is a medium priority task."
        if time_bound == 'yes':
            reminder_message += " It's time-bound."
            print("Reminder: " + reminder_message)
        else:
            print("Reminder: " + reminder_message)

    case 'low':
        if time_bound == 'no':
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
            print(reminder_message)
        else:
            reminder_message = f"Note: '{task}' is a low priority task. It's time-bound."
            print(reminder_message)
    case _:
        print("Invalid priority entered.")
