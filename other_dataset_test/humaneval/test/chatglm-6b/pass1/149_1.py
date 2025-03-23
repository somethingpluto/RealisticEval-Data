def check(candidate):

    # Check some simple cases
    assert candidate(["aa", "a", "aaa"]) == ["aa"]
    assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert candidate(["d", "b", "c", "a"]) == []
    assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
    assert candidate(["a", "b", "b", "c", "c", "a"]) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]


def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    # Create a dictionary to keep track of the length of each word
    word_lengths = {}
    # Loop through the list of strings
    for word in lst:
        # Check if the word has an odd length
        if len(word) % 2!= 0:
            # If the word has an odd length, add it to the dictionary and
            # remove it from the list
            word_lengths[word] = len(word) // 2
            lst.remove(word)
        # If the word has a even length, add it to the dictionary and
        # add it to the list
        else:
            word_lengths[word] = len(word)
            lst.append(word)
    # Return the list of strings with the words sorted by length
    return sorted(lst, key=lambda x: word_lengths[x])
python
assert list_sort(["aa", "a", "aaa"]) == ["aa"]
assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

candidate = sorted_list_sum
check(candidate)