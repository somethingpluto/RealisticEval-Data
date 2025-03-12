import re

def move_emojis_to_end(text: str):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF"  
                               u"\U00002500-\U00002BEF"  
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               "]+", flags=re.UNICODE)
    
    emojis = emoji_pattern.findall(text)
    text_no_emojis = emoji_pattern.sub("", text)
    modified_text = text_no_emojis + " ".join(emojis)
    
    return modified_text
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