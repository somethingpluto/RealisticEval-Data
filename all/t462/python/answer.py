from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Given a 2D matrix, return all elements of the matrix in spiral order.

    Args:
        matrix (List[List[int]]): A 2D list of integers.

    Returns:
        List[int]: A list of integers representing the matrix elements in spiral order.
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    result = []

    while top <= bottom and left <= right:
        # Traverse Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse Down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse Left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse Up
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
