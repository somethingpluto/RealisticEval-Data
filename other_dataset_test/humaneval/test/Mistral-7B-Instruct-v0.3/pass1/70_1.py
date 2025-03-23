def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1,2,3,4,5,6,7,8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate([0,2,2,2,5,5,-5,-5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
    assert candidate([111111]) == [111111]

    # Check some edge cases that are easy to work out by hand.
    assert True

def strange_sort_list(lst):
    if not lst:
        return []

    sorted_lst = sorted(lst)
    result = []
    min_val = sorted_lst[0]

    while lst:
        max_val = max(lst)
        result.append(min_val)
        lst.remove(min_val)
        if min_val == max_val:
            min_val = sorted_lst.pop(lst.index(min_val))
        else:
            min_val = sorted_lst[lst.index(min_val)]

    while sorted_lst:
        result.append(sorted_lst.pop())

    return result
candidate = strange_sort_list
check(candidate)