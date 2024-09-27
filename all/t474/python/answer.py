def are_siblings(tree, val1, val2):
    """
    Determines if two values are siblings in a binary tree represented as an array.

    :param tree: List[int], the binary tree level-order representation
    :param val1: int, first value to check for sibling relationship
    :param val2: int, second value to check for sibling relationship
    :return: bool, True if val1 and val2 are siblings, False otherwise
    """
    if val1 == val2:
        return False  # A node cannot be a sibling to itself

    try:
        # Find indices of the values
        index1 = tree.index(val1)
        index2 = tree.index(val2)

        # Check if they have the same parent
        return (index1 - 1) // 2 == (index2 - 1) // 2 and index1 != index2
    except ValueError:
        # One of the values is not in the tree
        return False
