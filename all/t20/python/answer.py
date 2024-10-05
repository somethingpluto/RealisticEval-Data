import re


def transform_parentheses(text: str) -> str:
    """

    Args:
        text (str):

    Returns:

    """
    # Regular expression to find patterns like (*...*)
    pattern = re.compile(r'\(\*(.*?)\*\)')

    # Function to replace matched patterns
    def remove_inner_asterisks(match):
        content = match.group(1).replace('*', '')
        return f'(*{content}*)'

    # Substitute the pattern in text with the processed content
    return pattern.sub(remove_inner_asterisks, text)
