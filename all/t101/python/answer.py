def is_break_time(start_time: str, end_time: str, current_time: str) -> bool:
    """
    Determines if the current time falls within the break time range.

    Args:
        start_time (str): The start time of the break in HH:MM format.
        end_time (str): The end time of the break in HH:MM format.
        current_time (str): The current time in HH:MM format.

    Returns:
        bool: Returns True if the current time is within the break time range, False otherwise.
    """
    # Split the time strings into hours and minutes
    start_hour, start_minute = map(int, start_time.split(':'))
    end_hour, end_minute = map(int, end_time.split(':'))
    current_hour, current_minute = map(int, current_time.split(':'))

    # Calculate total minutes since midnight
    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute
    current_total_minutes = current_hour * 60 + current_minute

    # Check if the current time falls within the break time range
    return start_total_minutes <= current_total_minutes <= end_total_minutes