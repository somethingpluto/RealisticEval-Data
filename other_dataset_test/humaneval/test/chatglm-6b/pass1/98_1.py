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

 
>>> count_upper('aBCdEf')
1

>>> count_upper('abcdefg')
0

>>> count_upper('dBBE')
0

candidate = count_upper
check(candidate)