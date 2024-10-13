def extract_json(response: str) -> str:
    """
    Extracts the first complete JSON object from a given string.

    The function looks for the first occurrence of an opening curly brace '{'
    and searches for the corresponding closing curly brace '}'. It tracks
    the balance of braces to ensure that the JSON object is complete.

    If a complete JSON object is found, it returns the substring that
    represents that object. If no opening brace is found or if the braces
    are unbalanced (i.e., incomplete), it returns an empty string.

    Args:
        response: The input string from which to extract the JSON object.

    Returns:
        A string containing the first complete JSON object, or an
        empty string if no complete object is found.
    """