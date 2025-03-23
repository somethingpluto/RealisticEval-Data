def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3
    assert candidate("aaabb") == 2
    assert candidate("aaaBb") == 1
    assert candidate("") == 0
 
split_words("Hello world!")
 
["Hello", "world!"]
 
split_words("Hello,world!")
 
["Hello", "world!"]
 
split_words("This is a string with multiple spaces and commas")
 
["This", "is", "a", "string", "with", "multiple", "spaces", "and", " commas"]
 
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Split the text on whitespace
    words = txt.split()
    # Split the words on commas
    words = [word for word in words if word.strip().split(",")[0]!= " "]
    # Return the number of words that match the desired pattern
    return len(words)

candidate = split_words
check(candidate)