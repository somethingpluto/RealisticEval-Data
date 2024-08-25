import unittest


class TestDivideList(unittest.TestCase):
    def test_even_division(self):
        lst = [1, 2, 3, 4, 5, 6]
        n = 3
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_uneven_division(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        n = 3
        expected = [[1, 2, 3], [4, 5], [6, 7]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_more_parts_than_items(self):
        lst = [1, 2, 3]
        n = 5
        expected = [[1], [2], [3], [], []]
        self.assertEqual(divide_list(lst, n), expected)

    def test_single_element(self):
        lst = [1]
        n = 1
        expected = [[1]]
        self.assertEqual(divide_list(lst, n), expected)

    def test_empty_list(self):
        lst = []
        n = 3
        expected = [[], [], []]
        self.assertEqual(divide_list(lst, n), expected)

def divide_list(lst, n):
    """
    Divide a list into n parts as evenly as possible. Excess elements are distributed to earlier sublists.

    Args:
    lst (list): The list to be divided.
    n (int): The number of parts to divide the list into.

    Returns:
    list of lists: A list containing n sublists, where each sublist represents a part of the original list.
    """
    # Total number of elements in the list
    L = len(lst)
    # Calculate the size of each part
    base_size = L // n
    # Calculate the number of sections that will have an additional element
    remainder = L % n

    result = []
    # Start index of the sublist
    start_index = 0

    for i in range(n):
        # Determine the size of the current part
        part_size = base_size + (1 if i < remainder else 0)
        # Append the sublist to the result list
        result.append(lst[start_index:start_index + part_size])
        # Update the start index for the next part
        start_index += part_size

    return result