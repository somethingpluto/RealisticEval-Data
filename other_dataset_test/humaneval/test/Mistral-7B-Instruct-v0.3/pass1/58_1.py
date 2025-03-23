

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []

def common(l1: list, l2: list):
    set1 = set(l1)
    set2 = set(l2)
    common_set = set1 & set2
    return sorted(list(common_set))
candidate = common
check(candidate)