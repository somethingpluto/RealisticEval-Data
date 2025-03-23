def check(candidate):

    # Check some simple cases
    assert candidate([1,2,4,3,5])==3
    assert candidate([1,2,4,5])==-1
    assert candidate([1,4,2,5,6,7,8,9,10])==2
    assert candidate([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert candidate([])==-1


def can_arrange(arr):
    if len(arr) <= 1:
        return -1
    
    prev = None
    curr = arr[0]
    
    for i in range(1, len(arr)):
        if curr >= prev:
            prev = curr
            curr = prev[1:]
            
    return curr

candidate = can_arrange
check(candidate)