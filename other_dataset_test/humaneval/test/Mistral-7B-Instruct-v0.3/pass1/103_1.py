def check(candidate):

    # Check some simple cases
    assert candidate(1, 5) == "0b11"
    assert candidate(7, 13) == "0b1010"
    assert candidate(964,977) == "0b1111001010"
    assert candidate(996,997) == "0b1111100100"
    assert candidate(560,851) == "0b1011000010"
    assert candidate(185,546) == "0b101101110"
    assert candidate(362,496) == "0b110101101"
    assert candidate(350,902) == "0b1001110010"
    assert candidate(197,233) == "0b11010111"


    # Check some edge cases that are easy to work out by hand.
    assert candidate(7, 5) == -1
    assert candidate(5, 1) == -1
    assert candidate(5, 5) == "0b101"

def rounded_avg(n, m):
    if n > m:
        return -1

    total = 0
    count = m - n + 1

    for i in range(n, m + 1):
        total += i

    avg = total // count

    # Rounding to the nearest integer
    if (total - avg * count) > count / 2:
        avg += 1

    binary_avg = format(avg, '0b')
    return binary_avg
candidate = rounded_avg
check(candidate)