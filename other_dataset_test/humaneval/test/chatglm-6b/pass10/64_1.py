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
    >>> vowels_count("acedy")
    3
    """
    # Test that the function returns the correct number of vowels
    assert vowels_count("abcde") == 2
    assert vowels_count("acedy") == 3
    
    # Test that the function correctly handles 'y' at the end of a word
    assert vowels_count("acedyy") == 3
    
    # Test that the function correctly handles words that contain 'y'
    assert vowels_count("acedyy_") == 3
    
    # Test that the function correctly handles words that contain 'i'
    assert vowels_count("acedy_ie") == 3
    
    # Test that the function correctly handles words that contain 'o'
    assert vowels_count("acedy_oo") == 3
    
    # Test that the function correctly handles words that contain 'a'
    assert vowels_count("acedy_AA") == 3

candidate = vowels_count
check(candidate)