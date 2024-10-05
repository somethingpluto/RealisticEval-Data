import re


def move_emojis_to_end(text: str) -> str:
    """
    Move the emoji expressions in the string to the end of the text.

    Args:
        text (str): The input string containing text and possibly emojis.

    Returns:
        str: The modified string with all emojis moved to the end.
    """
    # Regular expression pattern for capturing emojis
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+", flags=re.UNICODE)

    # Find all emojis in the text
    emojis = ''.join(emoji_pattern.findall(text))

    # Remove emojis from the text
    text_without_emojis = emoji_pattern.sub('', text)

    # Concatenate non-emoji text with extracted emojis
    return text_without_emojis + emojis
