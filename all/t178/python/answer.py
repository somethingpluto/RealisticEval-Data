def find_longest_non_decreasing_subsequence(nums):
    if nums is None or len(nums) == 0:
        return []

    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1s
    previous = [-1] * n  # Initialize previous array with -1s

    max_length = 1
    last_index = 0

    # Calculate the length of the longest non-decreasing subsequence
    for i in range(1, n):
        for j in range(i):
            if nums[i] >= nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                previous[i] = j

        # Update max_length and last_index
        if dp[i] > max_length:
            max_length = dp[i]
            last_index = i

    # Reconstruct the longest non-decreasing subsequence
    subsequence = []
    while last_index != -1:
        subsequence.insert(0, nums[last_index])  # Add to the beginning
        last_index = previous[last_index]

    return subsequence
