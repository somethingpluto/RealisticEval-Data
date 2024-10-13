def hill_sort(arr):
    """
    Function to perform Hill sort (Shell sort).

    :param arr: A list of integers to be sorted.
    """
    n = len(arr)  # Get the size of the array

    # Start with a large gap, then reduce the gap
    gap = n // 2  # Initial gap size
    while gap > 0:
        # Do a gapped insertion sort for this gap size
        for i in range(gap, n):
            # Save the value to be inserted
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp

        gap //= 2  # Reduce the gap size
