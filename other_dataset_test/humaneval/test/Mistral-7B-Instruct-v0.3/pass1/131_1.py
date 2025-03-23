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
    if n < 10:
        return n if n % 2!= 0 else 0

    product = 1
    digits_str = str(n)
    for digit in digits_str:
        if int(digit) % 2!= 0:
            product *= int(digit)

    return product or 0
candidate = digits
check(candidate)