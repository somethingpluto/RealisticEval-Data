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
    if len(lst1) == 0 or len(lst2) == 0:
        return "NO"

    even_count = 0
    for i in range(len(lst1)):
        if lst1[i] % 2 == 0:
            even_count += 1
            if even_count > len(lst1) // 2:
                return "YES"

    return "YES"

candidate = exchange
check(candidate)