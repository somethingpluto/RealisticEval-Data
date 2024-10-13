def bubble_sort(arr):
    """
    Implements the Bubble Sort algorithm.

    This function sorts an array of integers in ascending order using the Bubble Sort algorithm.
    The algorithm works by repeatedly stepping through the list, comparing adjacent elements, and
    swapping them if they are in the wrong order. The process is repeated until the list is sorted.

    :param arr: A list of integers to be sorted.
    """
    n = len(arr)  # Get the size of the array
    swapped = True  # Initialize swapped to enter the loop

    while swapped:
        swapped = False  # Reset swapped flag for this pass
        for i in range(1, n):  # Iterate through the array
            if arr[i - 1] > arr[i]:  # Compare adjacent elements
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Swap if in the wrong order
                swapped = True  # Set swapped to True if a swap occurred
        n -= 1  # Reduce the range of comparison, as the last element is now sorted
