def compare_arrays(arr1, arr2):
    """
    Compares two lists to determine if they contain the same unique elements, irrespective of order.
    This function utilizes sets to filter out duplicates and compare the unique elements of both lists.
    
    :param arr1: The first list to compare. Elements can be of any type.
    :param arr2: The second list to compare. Elements should be of the same type as the first list.
    :returns: Returns True if both lists contain the same unique elements, otherwise returns False.
    
    Example:
    >>> compare_arrays([1, 2, 2, 3], [3, 1, 2])
    True
    
    >>> compare_arrays(['a', 'b'], ['a', 'c'])
    False
    """
    set1 = set(arr1)
    set2 = set(arr2)
    
    if len(set1) != len(set2):
        return False
    
    for item in set1:
        if item not in set2:
            return False
            
    return True