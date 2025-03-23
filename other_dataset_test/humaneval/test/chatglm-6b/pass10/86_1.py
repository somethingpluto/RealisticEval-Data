def check(candidate):

    # Check some simple cases
    assert candidate('Hi') == 'Hi'
    assert candidate('hello') == 'ehllo'
    assert candidate('number') == 'bemnru'
    assert candidate('abcd') == 'abcd'
    assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
    assert candidate('') == ''
    assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
    # Check some edge cases that are easy to work out by hand.
    assert True

 
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ASCII value. Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    # Create a dictionary to store the order of words and blank spaces
    words = {}
     spaces = {}
    # Iterate over the characters in the string
    for c in s:
        # Check if the character is a word character
        if c in words:
            # Update the word character's index in the dictionary
            words[c].index(words[c]) += 1
        # Check if the character is a blank space
        elif c in spaces:
            # Update the blank space's index in the dictionary
            spaces[c].index(spaces[c]) -= 1
        # If the character is not a word character or a blank space, add it to the list of words
        else:
            words[c] += 1
    # Create a new string with the words and their ordering
    return ''.join(words)

candidate = anti_shuffle
check(candidate)