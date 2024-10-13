def count_words(s: str) -> int:
    """Count the number of words in a given string."""
    # Initialize a word count variable
    word_count = 0

    # Split the input string into words
    words = s.split()  # Create a list of words from the input string

    # Count each word
    for word in words:
        word_count += 1  # Increment the count for each word found

    return word_count  # Return the total word count