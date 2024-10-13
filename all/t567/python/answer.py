from datetime import datetime, timedelta


def get_relative_time(message_date: datetime) -> str:
    now = datetime.now()
    time_difference = now - message_date
    one_day = timedelta(days=1)

    # Calculate the number of days difference
    days_difference = time_difference // one_day

    # Check if the message was created today
    if days_difference == 0:
        return "Today"
    # Check if the message was created yesterday
    elif days_difference == 1:
        return "Yesterday"
    # Check if the message was created within the past week (not today or yesterday)
    elif days_difference < 7:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return days_of_week[message_date.weekday()]  # Get the day of the week
    # If the message was created earlier than one week ago
    else:
        # Format the date to a readable string (e.g., "MM/DD/YYYY")
        return message_date.strftime("%m/%d/%Y")