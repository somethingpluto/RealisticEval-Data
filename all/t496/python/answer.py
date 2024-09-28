import math

def pascal_triangle_row(i):
    """
    Generates the ith row of Pascal's Triangle.

    :param i: Row index (0-indexed)
    :return: A list representing the ith row of Pascal's Triangle
    """
    row = [math.comb(i, k) for k in range(i + 1)]
    return row
