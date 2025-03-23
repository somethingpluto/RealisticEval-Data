def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3
    assert candidate("aaabb") == 2
    assert candidate("aaaBb") == 1
    assert candidate("") == 0
def split_words(txt):
    words = txt.split()
    if not words:
        if txt.isalpha():
            return len([char for char in txt.lower() if ord(char) % 2 == 1])
        else:
            return txt

    return words
candidate = split_words
check(candidate)