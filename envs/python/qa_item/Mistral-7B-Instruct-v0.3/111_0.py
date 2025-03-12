from typing import List
import os

def convert_chat_to_markdown(chat: List[str], title: str = "ChatGPT Conversation") -> bytes:
    markdown_template = f"""
# {title}

{'\n'.join('
import unittest
from datetime import datetime
from unittest.mock import patch


class TestConvertChatToMarkdown(unittest.TestCase):

    def test_default_title(self):
        chat = ["Hello", "Hi there!"]
        blob = convert_chat_to_markdown(chat)
        expected_start = "# ChatGPT Conversation\n\n**Human:**\nHello\n\n***\n\n**Assistant:**\nHi there!\n\n***\n\nExported on "
        text = blob.text()  # Assuming blob has a text method that returns the string
        self.assertTrue(text.startswith(expected_start))

    def test_custom_title(self):
        chat = ["How are you?", "I'm doing well, thank you!"]
        title = "Friendly Chat"
        blob = convert_chat_to_markdown(chat, title)
        expected_start = "# Friendly Chat\n\n**Human:**\nHow are you?\n\n***\n\n**Assistant:**\nI'm doing well, thank you!\n\n***\n\nExported on "
        text = blob.text()  # Assuming blob has a text method that returns the string
        self.assertTrue(text.startswith(expected_start))

    def test_alternate_speakers(self):
        chat = ["Question?", "Answer.", "Another question?", "Another answer."]
        blob = convert_chat_to_markdown(chat)
        expected_content = "**Human:**\nQuestion?\n\n***\n\n**Assistant:**\nAnswer.\n\n***\n\n**Human:**\nAnother question?\n\n***\n\n**Assistant:**\nAnother answer.\n\n***\n\nExported on "
        text = blob.text()  # Assuming blob has a text method that returns the string
        self.assertIn(expected_content, text)

    @patch('your_module.datetime')
    def test_correct_timestamp(self, mock_datetime):
        chat = ["What's the time?", "It's now."]
        mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, 0)
        blob = convert_chat_to_markdown(chat)
        expected_end = "Exported on 2024-01-01 12:00:00."
        text = blob.text()  # Assuming blob has a text method that returns the string
        self.assertTrue(text.endswith(expected_end))

    def test_blob_type(self):
        chat = ["This is a test.js.", "Yes, it is."]
        blob = convert_chat_to_markdown(chat)
        self.assertEqual(blob.type, 'text/markdown')

if __name__ == '__main__':
    unittest.main()