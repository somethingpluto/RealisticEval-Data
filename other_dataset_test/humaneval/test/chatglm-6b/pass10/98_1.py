def check(candidate):

    # Check some simple cases
    assert candidate('aBCdEf')  == 1
    assert candidate('abcdefg') == 0
    assert candidate('dBBE') == 0
    assert candidate('B')  == 0
    assert candidate('U')  == 1
    assert candidate('') == 0
    assert candidate('EEEE') == 2

    # Check some edge cases that are easy to work out by hand.
    assert True


def count_upper(s):
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                count += 1
    return count

print(count_upper('aBCdEf'))  # Output: 1
print(count_upper('abcdefg'))  # Output: 0
print(count_upper('dBBE'))  # Output: 0

candidate = count_upper
check(candidate)