def two_sum(nums, target):
    """
    Finds two indices of numbers in the array that sum up to the target value.

    Args:
        nums (list[int]): The input array of integers.
        target (int): The target sum value.

    Returns:
        list[int]: A list containing the indices of the two numbers.

    Raises:
        ValueError: If no such indices are found.
    """
    # Create a dictionary to store numbers and their corresponding indices
    nums_map = {}

    # First loop to populate the dictionary
    for i in range(len(nums)):
        nums_map[nums[i]] = i

    # Second loop to find the two indices
    for i in range(len(nums)):
        complement = target - nums[i]  # Calculate the complement

        # Check if the complement exists and is not the same index
        if complement in nums_map and nums_map[complement] != i:
            return [i, nums_map[complement]]  # Return the indices

    # If no solution is found, raise an exception
    raise ValueError("No two sum solution")