def check(candidate):

    # Check some simple cases
    assert candidate([1,2,4,3,5])==3
    assert candidate([1,2,4,5])==-1
    assert candidate([1,4,2,5,6,7,8,9,10])==2
    assert candidate([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert candidate([])==-1


# Example input
arr = [1, 2, 4, 3, 5]

# Function returns 3
print(can_arrange(arr))

# Example input with -1 returned
arr = [1, 2, 3]

# Function returns -1
print(can_arrange(arr))

[1, 2, 4, 3, 5] = 3
[1, 2, 3] = -1

candidate = can_arrange
check(candidate)