import re
from collections import Counter
from typing import List, Dict


def word_filter_counter(text: str, filter_words: List[str]) -> Dict[str, int]:
    """
    Counts the occurrences of specified words in the given text.

    This function filters the words from the text based on the provided list,
    counts their occurrences, and returns a dictionary with the words in the
    order they were provided.

    Args:
        text (str): The input text from which to count words.
        filter_words (List[str]): A list of words to filter and count.

    Returns:
        Dict[str, int]: A dictionary with the count of each filter word in the text,
                         maintaining the order from filter_words.
    """
    # Convert filter words to lowercase for case-insensitive comparison
    filter_words_set = set(word.lower() for word in filter_words)

    # Find all words in the text using a regex pattern
    words = re.findall(r"\b\w+(?:'\w+)?\b", text.lower())

    # Count occurrences of filtered words
    word_counts = Counter(word for word in words if word in filter_words_set)

    # Create an ordered output based on the original order of filter_words
    ordered_output = {word: word_counts.get(word.lower(), 0) for word in filter_words}

    return ordered_output
