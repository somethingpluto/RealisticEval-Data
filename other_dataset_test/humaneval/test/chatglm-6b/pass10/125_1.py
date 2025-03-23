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
 
['Hello', 'world!']
 
split_words("abcdef")
 
['a', 'b', 'c', 'd', 'e', 'f']

candidate = split_words
check(candidate)