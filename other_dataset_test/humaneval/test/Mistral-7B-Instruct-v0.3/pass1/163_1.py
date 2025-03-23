def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
    assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
    assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
    assert candidate(17,89) == [], "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def generate_integers(a, b):
    as_str = str(a)
    bs_str = str(b)
    result = []
    for i in range(min(len(as_str), len(bs_str)), 0, -1):
        if len(as_str) - i < len(bs_str) - i:
            break
        if int(as_str[i - 1]) % 2 == 0 and int(bs_str[i - 1]) % 2 == 0:
            result.append(int(as_str[i - 1]))
            result.append(int(bs_str[i - 1]))
    return sorted(result)
candidate = generate_integers
check(candidate)