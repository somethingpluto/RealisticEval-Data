import unittest


class TestMoveEmojisToEnd(unittest.TestCase):

    def test_single_emoji_at_start(self):
        """ Test string with a single emoji at the start """
        input_text = "😊 Hello, world!"
        expected_output = " Hello, world!😊"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_multiple_emojis_mixed(self):
        """ Test string with multiple emojis mixed in text """
        input_text = "Ready 😊 to start 🚀 your day? 🌞"
        expected_output = "Ready  to start  your day? 😊🚀🌞"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_all_emojis(self):
        """ Test string that contains only emojis """
        input_text = "😊🚀🌞🎉"
        expected_output = "😊🚀🌞🎉"  # Output should remain the same as input
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_no_emojis(self):
        """ Test string with no emojis """
        input_text = "Hello, world!"
        expected_output = "Hello, world!"  # Output should remain the same as input
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_and_whitespace(self):
        """ Test string with emojis and whitespace characters """
        input_text = "🚀 Are we 😊 ready? 🌞  "
        expected_output = " Are we  ready?   🚀😊🌞"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

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
