

METADATA = {}


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []

 
common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
 
[1, 5, 653]
 
common([5, 3, 2, 8], [3, 2])
 
[2, 3]
 
common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121], sorted=True)
 
[1, 2, 5, 653, 3, 4, 7, 8, 9, 121]

candidate = common
check(candidate)