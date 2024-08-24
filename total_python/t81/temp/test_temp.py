import unittest

class TestFindClosestElement(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError, msg="Should raise ValueError for empty list"):
            find_closest_element(5, [])

    def test_basic_functionality(self):
        self.assertEqual(find_closest_element(5, [1, 3, 7, 8, 9]), 3, "Should return 3 as it is the first closest element to 5")

    def test_exact_match(self):
        self.assertEqual(find_closest_element(7, [1, 3, 7, 8, 9]), 7, "Should return 7 as it exactly matches the target")

    def test_multiple_closest_values(self):
        self.assertEqual(find_closest_element(5, [4, 6, 8, 9]), 4, "Should return 4 as it is the first closest element to 5")

    def test_float_values(self):
        self.assertEqual(find_closest_element(5.5, [1.1, 3.3, 7.7, 8.8]), 3.3, "Should return 3.3 as it is the first closest element to 5.5")


from typing import List, Union

def find_closest_element(target: Union[int, float], elements: List[Union[int, float]]) -> Union[int, float]:
    """
    Finds and returns the element from the given list that is closest to the specified target value.

    Args:
        target (Union[int, float]): The target number to which we want to find the closest element.
        elements (List[Union[int, float]]): A list of numerical elements from which the closest element is to be found.

    Returns:
        Union[int, float]: The element from the list that is closest to the target value.
    """
    if not elements:
        raise ValueError("The list of elements cannot be empty.")

    return min(elements, key=lambda x: abs(x - target))
