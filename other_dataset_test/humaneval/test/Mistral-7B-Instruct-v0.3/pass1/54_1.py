

METADATA = {}


def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False

def same_chars(s0: str, s1: str):
    if len(s0)!= len(s1):
        return False

    set_s0 = set(s0)
    set_s1 = set(s1)

    return set_s0 == set_s1
candidate = same_chars
check(candidate)