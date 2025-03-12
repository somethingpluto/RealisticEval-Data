def shell_sort(arr):
    """Shell sort function."""
    n = len(arr)  # Get the size of the array
    # Start with a large gap, then reduce the gap
    gap = n // 2  
    while gap > 0:
        # Perform a gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            # Put qa_item (the original arr[i]) in its correct location
            arr[j] = temp
        gap //= 2  # Reduce the gap