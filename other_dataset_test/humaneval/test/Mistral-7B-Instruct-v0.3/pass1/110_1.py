def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == "YES" 
    assert candidate([5, 7, 3], [2, 6, 4]) == "YES"
    assert candidate([5, 7, 3], [2, 6, 3]) == "NO" 
    assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([100, 200], [200, 200]) == "YES"

def exchange(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] % 2!= 0 and lst2[j] % 2 == 0:
                lst1[i], lst2[j] = lst2[j], lst1[i]
                for k in range(len(lst1)):
                    if lst1[k] % 2!= 0:
                        return "NO"
                return "YES"
    return "NO"
candidate = exchange
check(candidate)