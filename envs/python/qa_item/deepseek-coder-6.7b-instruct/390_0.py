from typing import List
import re

def split_into_sentences(text: str) -> List[str]:
    """
    Split the input text string into sentences.

    Args:
        text (str): The input text to be split into sentences.

    Returns:
        list: A list of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
    """
    # Use regex to split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    # Clean and strip each sentence
    cleaned_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return cleaned_sentences
import unittest


class TestSplitIntoSentences(unittest.TestCase):

    def test_basic_splitting(self):
        # Test splitting a basic text with clear punctuation
        text = "Hello world! How are you? I am fine."
        expected = ["Hello world!", "How are you?", "I am fine."]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_complex_punctuation(self):
        # Test splitting text that includes quotes and commas
        text = 'He said, This is amazing! Then he left.'
        expected = ['He said, This is amazing!', "Then he left."]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_with_no_punctuation(self):
        # Test text that has no punctuation marks
        text = "Hello world how are you"
        expected = ["Hello world how are you"]
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        # Test empty string input
        text = ""
        expected = []
        result = split_into_sentences(text)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()