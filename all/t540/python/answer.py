def generate_unique_pairs(array):
    """
    Generates all unique combinations of pairs from an array.

    :param array: The input list from which combinations are generated.
    :return: A list of lists, where each inner list contains a unique pair of elements.
    """
    pairs = []
    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            pairs.append([array[i], array[j]])
    return pairs
