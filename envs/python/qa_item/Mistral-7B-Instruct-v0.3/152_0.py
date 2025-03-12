def my_function(a, b, c=0):
    """
    This function performs a simple operation on three inputs.

    Args:
        a (int or float): The first input.
        b (int or float): The second input.
        c (int or float, optional): The third input. Defaults to 0.

    Returns:
        int or float: The result of the operation.
    """
    return a + b + c

if __name__ == '__main__':
    unittest.main()