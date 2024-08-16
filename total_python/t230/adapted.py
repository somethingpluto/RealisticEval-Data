import emoji


def move_emojis_to_end(text):
    """
    Moves all emojis in the text to the end of the string.

    Args:
    text (str): The input string containing text and possibly emojis.

    Returns:
    str: The modified string with all emojis moved to the end.
    """
    non_emojis = []
    emojis = []

    # Split the text into graphemes (characters including emoji which can be multiple code points)
    characters = [char for char in text]

    for char in characters:
        # Check if the character is an emoji
        if emoji.is_emoji(char):
            emojis.append(char)
        else:
            non_emojis.append(char)

    # Join non-emoji characters and emoji characters
    return ''.join(non_emojis) + ''.join(emojis)
