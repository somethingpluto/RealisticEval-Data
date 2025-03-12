def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEdy")
    3
    """
    # Test cases for 'y' at the end of a word
    if s.endswith("y"):
        assert vowels_count("abcde") == 2
        assert vowels_count("ACEdy") == 3
    else:
        # Test cases for other types of vowels
        assert vowels_count("ab") == 1
        assert vowels_count("cd") == 1
        assert vowels_count("de") == 2
        assert vowels_count("fi") == 1
        assert vowels_count("se") == 2
        assert vowels_count("ve") == 1

candidate = vowels_count
check(candidate)