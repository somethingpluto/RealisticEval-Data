def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


def closest_integer(value):
    if not value.isdigit():
        raise ValueError("The input value must be a string of digits")
    
    a, b = value.split()]
    distance = float(a - b)
    
    if distance < 0:
        distance += 1
    
     closest_integer = int(a) + distance
    
    return closest_integer

>>> closest_integer("10")
10
>>> closest_integer("15.3")
15
>>> closest_integer("14.5")
15
>>> closest_integer("-14.5")
-15

candidate = closest_integer
check(candidate)