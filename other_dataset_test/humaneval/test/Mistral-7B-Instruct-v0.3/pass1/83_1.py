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
    start_ones = 10 * 10 ** (n - 1)
    end_ones = 9 * 10 ** (n - 1) - 9 * 10 ** (n - 2) - 9 * 10 ** (n - 3) -... - 9
    return start_ones + end_ones
candidate = starts_one_ends
check(candidate)