def format_thread_count(count: int) -> str:
    """
    Formats the thread count into a user-friendly string.

    The function formats the number of threads into a two-digit string
    followed by "Thread" or "Threads" based on the count.

    For example:
        - Input: 3  Output: "03 Threads"
        - Input: 1  Output: "01 Thread"

    Args:
        count (int): The number of threads.

    Returns:
        str: A formatted string indicating the number of threads.
             The string will be in the format "XX Thread" or "XX Threads",
             where XX is the count formatted as a two-digit number.
    """