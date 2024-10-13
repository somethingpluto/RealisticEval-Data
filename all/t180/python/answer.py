def binary_search_closest(array, target):
    """
    Performs a binary search to find the index of the target value in a sorted array.
    If the target value is not found, it returns the index of the closest value.

    :param array: The sorted array in which to search.
    :param target: The target value to search for.
    :return: The index of the target or the index of the closest value if the target is not found.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # After the loop, left is the first index greater than the target
    # and right is the last index less than the target
    if left >= len(array):
        return len(array) - 1  # closest is the last element
    if right < 0:
        return 0  # closest is the first element

    # Check which is closer: array[left] or array[right]
    if abs(array[left] - target) < abs(array[right] - target):
        return left
    else:
        return right
