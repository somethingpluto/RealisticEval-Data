def check(candidate):

    # Check some simple cases
    assert candidate((1, 2), (2, 3)) == "NO"
    assert candidate((-1, 1), (0, 4)) == "NO"
    assert candidate((-3, -1), (-5, 5)) == "YES"
    assert candidate((-2, 2), (-4, 0)) == "YES"

    # Check some edge cases that are easy to work out by hand.
    assert candidate((-11, 2), (-1, -1)) == "NO"
    assert candidate((1, 2), (3, 5)) == "NO"
    assert candidate((1, 2), (1, 2)) == "NO"
    assert candidate((-2, -2), (-3, -2)) == "NO"


interval1 = (1, 2)
interval2 = (2, 3)

print(intersection(interval1, interval2))  # Output: "YES"
python
interval1 = (-1, 1)
interval2 = (0, 4)

print(intersection(interval1, interval2))  # Output: "NO"
python
interval1 = (-3, -1)
interval2 = (-5, 5)

print(intersection(interval1, interval2))  # Output: "YES"

candidate = intersection
check(candidate)