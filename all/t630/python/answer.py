def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # Current element to be inserted into sorted portion
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key