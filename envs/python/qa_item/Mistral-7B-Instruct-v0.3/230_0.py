import re

def move_emojis_to_end(text: str):
    emoji_pattern = re.compile(r'['
                               u'\U0001F600-\U0001F64F'
                               u'\U0001F300-\U0001F5FF'
                               u'\U0001F680-\U0001F6FF'
                               u'\U0001F1E0-\U0001F1FF'
                               u'\U00002700-\U000027BF'
                               u'\U000024C2-\U0001F251'
                               u'\U0001F926-\U0001F937'
                               u'\U0001F60A-\U0001F60D'
                               u'\U0001F6B0-\U0001F6B6'
                               u'\U0000267F-\U000026FE'
                               u'\U00002702-\U00002744'
                               u'\U00002747-\U0000274E'
                               u'\U00002753-\U00002757'
                               u'\U00002763-\U00002767'
                               u'\U00002795-\U0000279F'
                               u'\U0001F330-\U0001F5FF'
                               u'\U0001F690-\U0001F6C1'
                               u'\U0001F900-\U0001F9FF'
                               u'\U0001F600-\U0001F64F'
                               u'\U0001F680-\U0001F6FF'
                               u'\U0001F1E0-\U0001F1FF'
                               u'\U00002702-\U000027B0'
                               u'\U00002458-\U0000245C'
                               u'\U000023CF-\U000023D2'
                               u'\U0000231A-\U0000231F'
                               u'\U0000203C-\U00002040'
                               u'\U00002070-\U00002074'
                               u'\U00002021-\U0000202A'
                               u'\U00002030-\U00002039'
                               u'\U00002049-\U0000204D'
                               u'\U00002000-\U0000206F'
                               u'\U0000A9-\U0000D7FF'
                               u'\U0000E000-\U0010FFFF'
                               r']')

    emoji_start = re.search(emoji_pattern, text)
    if emoji_start:
        emoji_end = text[emoji_start.end():]
        text = text[:emoji_start.start()] + text[emoji_start.end():]
        return text + emoji_end
    else:
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