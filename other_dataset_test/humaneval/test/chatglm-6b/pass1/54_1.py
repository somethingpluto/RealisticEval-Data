

METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False


>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
True

>>> same_chars('abcd', 'dddddddabc')
True

>>> same_chars('dddddddabc', 'abcd')
True

>>> same_chars('eabcd', 'dddddddabc')
False

>>> same_chars('abcd', 'dddddddabce')
False

>>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
False

candidate = same_chars
check(candidate)