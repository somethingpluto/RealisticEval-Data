import re


def remove_inner_asterisks(text: str) -> str:
    """
    Transforms the input text by finding and modifying patterns that match the format '(*...*)'.
    Specifically, it removes any asterisks inside the parentheses while preserving the outer format.
    For example:
        input: *he*l*lo*
        output: *hello*

    Args:
        text (str): The input text containing patterns to be transformed.

    Returns:
        str: The transformed text with asterisks inside '(*...*)' patterns removed.
    """

    # Regular expression to find patterns like (*...*)
    pattern = re.compile(r'\(\*(.*?)\*\)')

    # Function to replace matched patterns
    def remove_inner_asterisks(match):
        content = match.group(1).replace('*', '')
        return f'(*{content}*)'

    # Substitute the pattern in text with the processed content
    return pattern.sub(remove_inner_asterisks, text)
