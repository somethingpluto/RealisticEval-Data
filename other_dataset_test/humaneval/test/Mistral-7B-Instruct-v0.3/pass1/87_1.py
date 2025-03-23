def check(candidate):

    # Check some simple cases
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
    ], 2) == [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
    assert candidate([
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,1,3,4,5,6],
        [1,2,1,4,5,6],
        [1,2,3,1,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 0), (2, 1), (2, 0), (3, 2), (3, 0), (4, 3), (4, 0), (5, 4), (5, 0), (6, 5), (6, 0)]
    assert candidate([], 1) == []
    assert candidate([[1]], 2) == []
    assert candidate([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    # Check some edge cases that are easy to work out by hand.
    assert True

def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, val in enumerate(row):
            if val == x:
                result.append((i, j))

    # Sort the results by row in ascending order and then by column in descending order
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
candidate = get_row
check(candidate)