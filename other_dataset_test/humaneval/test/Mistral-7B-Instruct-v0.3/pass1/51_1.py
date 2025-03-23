

METADATA = {}


def check(candidate):
    assert candidate('') == ''
    assert candidate("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert candidate('fedcba') == 'fdcb'
    assert candidate('eeeee') == ''
    assert candidate('acBAA') == 'cB'
    assert candidate('EcBOO') == 'cB'
    assert candidate('ybcd') == 'ybcd'

def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join(c for c in text if c not in vowels)
candidate = remove_vowels
check(candidate)