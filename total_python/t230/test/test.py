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
