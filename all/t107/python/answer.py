import random

def find_median(arr):
    """
    Finds the median of a given array of numbers.

    Args:
        arr (list of float): The array of numbers to find the median of.

    Returns:
        float: The median of the array.
    """
    # Sort the array in ascending order
    arr.sort()

    n = len(arr)
    mid_index = n // 2  # Use integer division to find the middle index

    # Determine if the array length is even or odd and return the median
    if n % 2 == 0:
        # Even number of elements: average the two middle elements
        return (arr[mid_index - 1] + arr[mid_index]) / 2
    else:
        # Odd number of elements: return the middle element
        return arr[mid_index]
