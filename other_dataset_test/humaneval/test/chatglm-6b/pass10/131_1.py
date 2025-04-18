def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


def digits(n):
    if n % 10 == 0:
        return 1
    else:
        return n // 10 * digits(n // 10)

candidate = digits
check(candidate)