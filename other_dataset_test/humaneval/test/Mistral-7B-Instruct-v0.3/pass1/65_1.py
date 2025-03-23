def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"

def circular_shift(x, shift):
    # Convert the number to a string
    num_str = str(x)

    # Calculate the number of digits
    num_digits = len(num_str)

    # Shift the digits to the right
    shifted_num_str = num_str[shift:] + num_str[:shift]

    # If the shift is greater than the number of digits, return the reversed digits
    if shift > num_digits:
        return shifted_num_str[num_digits - shift:] + shifted_num_str[:num_digits - shift]

    # Return the shifted number as a string
    return shifted_num_str
candidate = circular_shift
check(candidate)