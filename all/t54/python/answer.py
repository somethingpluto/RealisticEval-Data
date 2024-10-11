def remove_triple_backticks(string_list):
    """
    Processes a list of strings, removing all occurrences of three consecutive backticks from each string.

    Args:
    string_list (list of str): The list of strings to process.

    Returns:
    list of str: A new list with all instances of three consecutive backticks removed from each string.
    """
    # Use list comprehension to process each string in the list by removing three consecutive backticks
    processed_list = [s.replace('```', '') for s in string_list]
    return processed_list
