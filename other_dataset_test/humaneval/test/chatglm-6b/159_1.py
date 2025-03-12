def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(5, 6, 10) == [11, 4], "Error"
    assert candidate(4, 8, 9) == [12, 1], "Error"
    assert candidate(1, 10, 10) == [11, 0], "Error"
    assert candidate(2, 11, 5) == [7, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(4, 5, 7) == [9, 2], "Error"
    assert candidate(4, 5, 1) == [5, 0], "Error"


# Example usage
eat(5, 6, 10)
print(f"You have eaten 5 carrots and are now {number} carrots remaining.")

# Example usage with a larger number of carrots
eat(10, 8, 12)
print(f"You have eaten 10 carrots and are now {number} carrots remaining.")

# Example usage with a smaller number of carrots
eat(3, 10, 5)
print(f"You have eaten 3 carrots and are now {number} carrots remaining.")

You have eaten 5 carrots and are now 3 carrots remaining.
You have eaten 10 carrots and are now 5 carrots remaining.
You have eaten 3 carrots and are now 0 carrots remaining.

candidate = eat
check(candidate)