def merge(arr, left, mid, right):
    n1 = mid - left + 1  # Size of the left subarray
    n2 = right - mid     # Size of the right subarray
    
    # Create temporary arrays
    L = arr[left:mid + 1]  # Copy data to temporary arrays L[]
    R = arr[mid + 1:right + 1]  # Copy data to temporary arrays R[]
    
    # Merge the temporary arrays back into arr[left..right]
    i = 0  # Initial index of the first subarray
    j = 0  # Initial index of the second subarray
    k = left  # Initial index to be sorted

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        # Same as (left + right) // 2, but avoids overflow for large left and right
        mid = left + (right - left) // 2
        
        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)