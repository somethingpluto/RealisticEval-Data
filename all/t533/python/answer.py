import random


def shuffle_string(input_string: str) -> str:
    """Shuffles the characters in a given string randomly.

    Args:
        input_string (str): The string to shuffle.

    Returns:
        str: A new string with the characters shuffled.
    """
    # Convert the string into a list of characters
    char_list = list(input_string)

    # Shuffle the list using the Fisher-Yates algorithm
    length = len(char_list)
    for i in range(length - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        random_index = random.randint(0, i)  # random.randint includes both endpoints
        # Swap the current character with the character at the random index
        char_list[i], char_list[random_index] = char_list[random_index], char_list[i]

    # Join the shuffled list back into a string and return it
    return ''.join(char_list)