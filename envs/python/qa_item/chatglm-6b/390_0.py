
from typing import List

def split_into_sentences(text: str) -> List[str]:
    """
    Split the input text string into sentences.

    Args:
        text (str): The input text to be split into sentences.

    Returns:
        list: A list of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
    """
    # Split the text into words using the'split' method
    words = text.split()

    # Iterate over the words and extract sentences
    sentences = []
    for word in words:
        if word.isspace():
            # Remove leading/trailing whitespace
            sentences.append(word.strip())
        else:
            # Add the sentence to the list
            sentences.append(word)

    return sentences

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