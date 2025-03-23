def check(candidate):

    # Check some simple cases
    assert candidate(3) == [3, 5, 7], "Test 3"
    assert candidate(4) == [4,6,8,10], "Test 4"
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def make_a_pile(n):
    pile = [n]
    level = n
    while level > 1:
        if level % 2 == 1:
            level += 1
        else:
            level += 2
        pile.append(level)
        level //= 2
    return pile
candidate = make_a_pile
check(candidate)