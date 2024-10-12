def greet(name):
    """
    Greets someone with a personalized message.

    Logs a personalized greeting message, using the provided name as input.

    Args:
        name (str): The name to include in the personalized message.
    """
    if not isinstance(name, str) or not name.strip():
        print('Hello, Guest!')
    else:
        print(f'Hello, {name.strip()}!')


def sum(arr):
    """
    Calculates the sum of all elements in an array.

    Takes a list of numbers as input and returns the sum of all the elements.
    If the list is empty, it returns 0.

    Args:
        arr (list): The list of numbers to sum.

    Returns:
        int: The sum of all elements of the list.

    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(arr, list):
        raise TypeError('Expected an array of numbers')

    return sum(arr)