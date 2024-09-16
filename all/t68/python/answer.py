def divide_list(lst, n):
    """
    Divide a list into n parts as evenly as possible. Excess elements are distributed to earlier sublists.

    Args:
    lst (list): The list to be divided.
    n (int): The number of parts to divide the list into.

    Returns:
    list of lists: A list containing n sublists, where each sublist represents a part of the original list.
    """
    # Total number of elements in the list
    L = len(lst)
    # Calculate the size of each part
    base_size = L // n
    # Calculate the number of sections that will have an additional element
    remainder = L % n

    result = []
    # Start index of the sublist
    start_index = 0

    for i in range(n):
        # Determine the size of the current part
        part_size = base_size + (1 if i < remainder else 0)
        # Append the sublist to the model_result list
        result.append(lst[start_index:start_index + part_size])
        # Update the start index for the next part
        start_index += part_size

    return result