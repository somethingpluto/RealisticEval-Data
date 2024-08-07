def closest_num(num, num_list):
    """
    Given a number and a list of numbers, returns the number from the list
    that is closest to the given number.
    (Written by ChatGPT)
    """
    closest = None
    diff = float('inf')  # Initialize with a very large number

    for n in num_list:
        if abs(num - n) < diff:
            diff = abs(num - n)
            closest = n

    return closest