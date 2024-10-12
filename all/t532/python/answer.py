def count_letter_changes(input_string: str) -> list:
    """Counts the occurrences of consecutive identical letters in a given string.

    Args:
        input_string (str): The string to analyze for letter changes.

    Returns:
        list: A list of counts representing the number of consecutive
              identical letters before a different letter is found.
    """
    # List to hold counts of consecutive letters
    counts = []
    current_count = 1  # Initialize the count of the current letter

    # Iterate through the string starting from the second character
    for i in range(1, len(input_string)):
        # If the current character is different from the previous one
        if input_string[i] != input_string[i - 1]:
            counts.append(current_count)  # Store the count of the previous letter
            current_count = 1  # Reset count for the new letter
        else:
            current_count += 1  # Increment count for the current letter

    counts.append(current_count)  # Push the count of the last letter
    return counts
