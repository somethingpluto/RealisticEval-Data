def look_and_say(number:str):
    """
    Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
    grouping by consecutive digits.

    Args:
        number (str): The current sequence as a string.

    Returns:
        str: The next sequence in the 'look-and-say' series.
    """
    result = []
    count = 1
    length = len(number)

    # Iterate through the number, group by consecutive digits and count them
    for i in range(1, length):
        if number[i] == number[i - 1]:
            count += 1
        else:
            result.append(f"{count}{number[i - 1]}")
            count = 1

    # Append the last group of digits
    result.append(f"{count}{number[-1]}")

    return ''.join(result)