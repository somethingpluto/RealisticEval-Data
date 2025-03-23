def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"

import math

def closest_integer(value):
    number = float(value)
    if number >= 0:
        return math.floor(number + 0.5) if number - math.floor(number) >= 0.5 else math.floor(number)
    else:
        return math.ceil(number - 0.5) if math.ceil(number) - number >= 0.5 else math.ceil(number)
candidate = closest_integer
check(candidate)