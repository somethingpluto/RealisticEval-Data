def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


def starts_one_ends(n):
    count = 0
    for i in range(n):
        if i % 10 == 0 and i > 0:
            if i == 1:
                count += 1
            elif i == 9:
                count -= 1
    return count

candidate = starts_one_ends
check(candidate)