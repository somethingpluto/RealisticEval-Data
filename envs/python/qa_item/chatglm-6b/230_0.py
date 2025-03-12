
import re

def move_emojis_to_end(text: str) -> str:
    # Replace all emojis with their ASCII codes
    emojis = re.findall(r'[\u4e00-\u9fa5]+', text)
    
    # Move the emojis to the end of the string
    text = text.replace(emojis, '👀')
    
    return text

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