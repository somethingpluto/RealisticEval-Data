def snake_to_camel(snake_str):
    """
    Convert a snake_case string to CamelCase.

    Parameters:
    snake_str (str): The snake_case string to convert.

    Returns:
    str: The converted CamelCase string.
    """
    # Split the snake_case string into words
    words = snake_str.split('_')
    # Capitalize the first letter of each word and join them
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str