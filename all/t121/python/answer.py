def adjust_array_length(target_length, array):
    array_length = len(array)  # Get the length of the array

    if array_length == target_length:
        return array  # If the array length matches the target, return the array

    if array_length < target_length:
        # Calculate how many times to repeat the array and flatten it
        repeated_array = (array * ((target_length // array_length) + 1))[:target_length]
        return repeated_array

    # If the array is longer than the target length, slice it
    return array[:target_length]