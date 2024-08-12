def find_largest_divisible(n):
    """
    find the largest integer between a given number n and half of it that is divisible by 10 or 5
    Args:
        n (int): The upper bound of the range.

    Returns:
        The largest integer between n and half of n that is divisible by 5, or
         None if no such number exists.
    """
    # Start checking from n and go down to half of n
    start = n
    end = n // 2

    for i in range(start, end, -1):
        if i % 5 == 0:
            return i

    return None  # Return None if no number divisible by 5 is found
