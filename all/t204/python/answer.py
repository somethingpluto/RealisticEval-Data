def split_string(s: str) -> list[str]:
    """
    Split the input string into a list of words.

    :param s: The string to be split.
    :return: A list of words obtained from the input string.
    """
    result = []
    words = s.split()  # Split the string by whitespace
    for word in words:
        result.append(word)  # Add each word to the result list
    return result