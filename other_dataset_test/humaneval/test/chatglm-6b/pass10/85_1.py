def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

# input list
lst = [4, 2, 6, 7]

# add the even elements that are at odd indices
add(lst)

# output list
print(add(lst))
# Output: [2, 2, 2, 2]

candidate = add
check(candidate)