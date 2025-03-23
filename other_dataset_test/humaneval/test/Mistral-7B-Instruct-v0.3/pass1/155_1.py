def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)


    # Check some edge cases that are easy to work out by hand.
    assert True

def even_odd_count(num):
    if num < 0:
        num *= -1

    count_even = 0
    count_odd = 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num //= 10

    return count_even, count_odd
candidate = even_odd_count
check(candidate)