def find_max_difference(l):
    """
    Finds the maximum difference between elements in the array
    such that the smaller element appears before the larger one.

    :param l: A list of integers containing the elements.
    :return: The maximum difference.
    """
    min_val = l[0]
    max_diff = float('-inf')  # Initialize to negative infinity

    for i in range(1, len(l)):
        max_diff = max(max_diff, l[i] - min_val)
        min_val = min(min_val, l[i])

    return max_diff
