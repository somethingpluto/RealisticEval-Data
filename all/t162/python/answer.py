def bool_array_to_binary_string(bool_array):
    """
    Converts the array of Boolean values to a binary string representation,
    which converts to the character '1' if the Boolean value is true.
    Otherwise, it is converted to the character '0', and the final string is returned.

    Args:
        bool_array (list[bool]): An array of boolean values.

    Returns:
        str: A binary string where '1' represents true and '0' represents false.
    """
    return ''.join('1' if bool_val else '0' for bool_val in bool_array)
