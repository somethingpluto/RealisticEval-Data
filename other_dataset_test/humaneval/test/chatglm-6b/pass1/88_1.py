def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == [], "Error"
    assert candidate([5]) == [5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([2, 1]) == [1, 2], "Error"
    assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
    assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"


array = [5, 2, 4, 3, 0, 1, 5, 6]
sorted_array = sort_array(array)
print(sorted_array)

[0, 1, 2, 3, 4, 5, 6]

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5, 6, -10]) => [-10, -9, -8, -7, -6, -5, -4, -3, -2]
    * sort_array([2, 4, 3, 0, 1, 5, 6, -10, -20]) => [-10, -20, -10, -10, -10, -10, -10, -10, -10, -10, -10]
    """
    if array[-1] < array[0]:
        return sorted_array(array[:-1]) + array[-1]
    else:
        return sorted_array(array[::-1]) - array[0]

candidate = sort_array
check(candidate)