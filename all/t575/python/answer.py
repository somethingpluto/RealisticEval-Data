def format_thread_count(count):
    """Formats the thread count into a user-friendly string.

    Args:
        count (int): The number of threads.

    Returns:
        str: A formatted string indicating the number of threads.
    """
    # Handle the case when there are no threads
    if count == 0:
        return "No Threads"

    # Convert the count to a string and pad it to ensure at least 2 digits
    thread_count = str(count).zfill(2)  # zfill pads the string with zeros

    # Determine the correct word form based on the count
    thread_word = "Thread" if count == 1 else "Threads"

    # Return the formatted string
    return f"{thread_count} {thread_word}"
