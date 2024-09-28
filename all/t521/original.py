def word_filter_counter(text, filter_words):
    # Your code goes here
    # Implement the logic to filter words and count their occurrences

    # covert filter_words into lower case
    filter_words_set = set(word.lower() for word in filter_words)

    # find all words
    words = re.findall(r'\b\w+(?:\'\w+)?\b', text.lower())
    """
                    This regex equation is written by ChatGPT.
                    I want to consider the complex situation, for example: I'll go to the school. I'll go to the park.
                    according to the instruction, I think the word "I'll" should be considered as a whole word. It means that "I" and "ll" should not be counted separately.
    """

    # 使用 Counter 计数
    word_counts = Counter(word for word in words if word in filter_words_set)

    # 结果有序输出，按照 filter_words 的顺序
    ordered_output = {word: word_counts.get(word.lower(), 0) for word in filter_words}
    return ordered_output
