def check(candidate):

    # Check some simple cases
    assert candidate(123) == (8, 13)
    assert candidate(12) == (4, 6)
    assert candidate(3) == (1, 2)
    assert candidate(63) == (6, 8)
    assert candidate(25) == (5, 6)
    assert candidate(19) == (4, 6)
    assert candidate(9) == (4, 5), "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == (0, 1), "This prints if this assert fails 2 (also good for debugging!)"

def even_odd_palindrome(n):
    evens = 0
    odds = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            evens += 1
        elif str(i) == str(i)[::-1] and i % 2!= 0:
            odds += 1
    return evens, odds
candidate = even_odd_palindrome
check(candidate)