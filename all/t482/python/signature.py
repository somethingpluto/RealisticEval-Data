def extract_outermost_brackets(s: str) -> str:
    """
    Extracts the contents of the outermost brackets from the input string.
    For example:
        input: Text [with [nested] brackets] and more text
        output: with [nested] brackets
    Args:
        s (str): The input string containing brackets.

    Returns:
        str: The contents within the outermost brackets, or an empty string if no brackets are found.
    """
