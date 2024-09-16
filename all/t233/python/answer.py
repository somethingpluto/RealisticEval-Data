def remove_comments(string: str) -> str:
    """
    Removes comments from the provided string. Comments start with a '#' and end at the newline.

    Args:
    string (str): The input string containing potential comments.

    Returns:
    str: The string with all comments removed.
    """
    lines = string.split('\n')  # Split the string into lines
    cleaned_lines = [line.split('#')[0] for line in lines]  # Remove the comment part from each line
    return '\n'.join(cleaned_lines)  # Join the lines back into a single string
