from typing import List

def get_palindrome_list(n: int) -> List[int]:
    """
    Filter out the number of palindrome within any number n. Palindrome numbers are numbers with the same correction and reverse readings, such as 121, 1331

    Args:
        n (int): range number

    Returns:
        List[int]: Palindrome numbers
    """
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    return [num for num in range(n) if is_palindrome(num)]
import unittest


class TestNthPalindrome(unittest.TestCase):
    def test_single_digit(self):
        """Test case for the first palindrome"""
        self.assertEqual(get_palindrome_list(1), [0], "The first palindrome should be 0")

    def test_edge_of_single_and_double_digits(self):
        """Test case for the tenth palindrome, transitioning to double digits"""
        self.assertEqual(get_palindrome_list(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "The tenth palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_edge_of_double_and_triple_digits(self):
        """Test case for the 100th palindrome, transitioning to triple digits"""
        self.assertEqual(get_palindrome_list(100), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99],
                         "The 100th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]")

    def test_large_number(self):
        """Test case for a larger number, e.g., the 1000th palindrome"""
        self.assertEqual(get_palindrome_list(1000),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141,
                          151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333,
                          343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525,
                          535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717,
                          727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909,
                          919, 929, 939, 949, 959, 969, 979, 989, 999]
                         ,
                         "The 1000th palindrome should be [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494, 505, 515, 525, 535, 545, 555, 565, 575, 585, 595, 606, 616, 626, 636, 646, 656, 666, 676, 686, 696, 707, 717, 727, 737, 747, 757, 767, 777, 787, 797, 808, 818, 828, 838, 848, 858, 868, 878, 888, 898, 909, 919, 929, 939, 949, 959, 969, 979, 989, 999]")

if __name__ == '__main__':
    unittest.main()