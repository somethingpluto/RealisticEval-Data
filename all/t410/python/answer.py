def check_xor_sum(combination):
    """
    Checks the XOR sums of specific columns in a given combination array.

    Args:
        combination (np.ndarray): A 2D numpy array where each column corresponds
                                  to a specific value.

    Returns:
        bool: True if the XOR sums of the specified columns match the required
              values; otherwise, False.
    """
    combination = combination.astype(int)  # Ensure that combination is an array of integers

    # Calculate XOR sums for specified columns
    xor_sum_0_3_6 = combination[:, 0] ^ combination[:, 3] ^ combination[:, 6]
    xor_sum_1_4_7 = combination[:, 1] ^ combination[:, 4] ^ combination[:, 7]
    xor_sum_2_5 = combination[:, 2] ^ combination[:, 5]

    # Check if the XOR sums match the expected values
    return (np.all(xor_sum_0_3_6 == 0x6b) and
            np.all(xor_sum_1_4_7 == 0x76) and
            np.all(xor_sum_2_5 == 0x12))