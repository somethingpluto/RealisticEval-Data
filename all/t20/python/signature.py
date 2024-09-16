def process_markdown(s: str) -> str:
    """
    processing the content of the Markdown file, remove unnecessary asterisks from the string and keep only the outermost asterisks. For example,"*some*text*" becomes "* sometime *"

    Args:
        s (str): The input string containing markdown-style asterisks.

    Returns:
        str: The processed string with asterisks removed, except for the first and last ones.
    """
