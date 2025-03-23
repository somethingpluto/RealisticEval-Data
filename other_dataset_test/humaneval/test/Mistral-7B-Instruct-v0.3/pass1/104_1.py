def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True

def has_even_digit(n):
    """Check if a number has any even digit."""
    return any(digit % 2 == 0 for digit in str(n))

def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit."""
    return sorted([num for num in x if not has_even_digit(num)])
candidate = unique_digits
check(candidate)