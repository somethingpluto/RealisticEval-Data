

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []


def common(l1: list, l2: list) -> list:
    if len(l1)!= len(l2):
        raise ValueError("The lists must have the same length.")

    common_elements = [None] * len(l1)

    for i in range(len(l1)):
        common_elements[l1[i]] = i

    for i in range(len(l2)):
        common_elements[l2[i]] = i

    return sorted(common_elements, key=lambda x: x)
python
l1 = [1, 4, 3, 34, 653, 2, 5]
l2 = [5, 7, 1, 5, 9, 653, 121]
common_elements = common(l1, l2)
print(common_elements)
python
[1, 5, 653]

candidate = common
check(candidate)