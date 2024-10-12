import time


def time_passed(start_time_in_millis: int) -> str:
    """
    Calculate the time passed since the start time in milliseconds and return a formatted string.

    Args:
        start_time_in_millis (int): The start time in milliseconds.

    Returns:
        str: A string representing the time passed in the format 'minutes:seconds'.
    """
    # Get the current time in milliseconds
    current_time_in_millis = int(time.time() * 1000)

    # Calculate the difference in milliseconds
    time_difference = current_time_in_millis - start_time_in_millis

    # Convert the difference to seconds
    total_seconds = time_difference // 1000

    # Calculate minutes and seconds
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    # Return the formatted string
    return f"{minutes}:{seconds:02}"
