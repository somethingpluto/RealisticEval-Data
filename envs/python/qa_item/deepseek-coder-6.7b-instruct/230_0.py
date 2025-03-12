import re

def move_emojis_to_end(text: str) -> str:
    """
    Move the emoji expressions in the string to the end of the text.

    Args:
        text (str): The input string containing text and possibly emojis.

    Returns:
        str: The modified string with all emojis moved to the end.
    """
    # Regular expression to match emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"  # enclosed characters
        "]+",
        flags=re.UNICODE
    )
    
    # Find all emojis in the text
    emojis = emoji_pattern.findall(text)
    
    # Remove emojis from the original text
    text_without_emojis = emoji_pattern.sub("", text)
    
    # Join the text without emojis with the emojis at the end
    return text_without_emojis + "".join(emojis)
import unittest


class TestMoveEmojisToEnd(unittest.TestCase):

    def test_no_emojis(self):
        # Case: String with no emojis
        input_text = "This is a test."
        expected_output = "This is a test."
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_all_emojis(self):
        # Case: String with only emojis
        input_text = "😀😃😄😁"
        expected_output = "😀😃😄😁"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_at_start(self):
        # Case: Emojis at the start of the text
        input_text = "😀😃Hello world!"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_at_end(self):
        # Case: Emojis already at the end of the text
        input_text = "Hello world!😀😃"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_emojis_in_middle(self):
        # Case: Emojis in the middle of the text
        input_text = "Hello 😀world😃!"
        expected_output = "Hello world!😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

    def test_mixed_characters(self):
        # Case: Text with mixed characters and emojis
        input_text = "Hi! 😀 How are you? 😃"
        expected_output = "Hi!  How are you? 😀😃"
        self.assertEqual(move_emojis_to_end(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()