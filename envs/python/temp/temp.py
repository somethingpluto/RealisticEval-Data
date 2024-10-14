def josephus(n, k):
    """
    Simulates the Josephus problem using a list to represent the circle of people.

    :param n: The number of people in the circle (1 to n).
    :param k: The step count (every k-th person will be eliminated).
    :return: The position of the last person remaining (1-indexed).
    """

    # Step 1: Create a list to represent the people in the circle
    people = list(range(1, n + 1))  # Create a list of people from 1 to n
    index = 0  # Start from the first person

    # Step 2: Eliminate people until only one remains
    while len(people) > 1:
        # Step 3: Find the index of the person to eliminate
        index = (index + k - 1) % len(people)  # -1 to adjust for zero-based index
        eliminated_person = people.pop(index)  # Eliminate that person
        print(f"Eliminated: {eliminated_person}, Remaining: {people}")

    # Step 4: Return the position of the last remaining person
    return people[0]  # The last remaining person

# Unit Test Class
import unittest


class TestJosephusProblem(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(josephus(7, 3), 4)  # Standard case

    def test_case_2(self):
        self.assertEqual(josephus(1, 1), 1)  # Only one person

    def test_case_3(self):
        self.assertEqual(josephus(5, 2), 3)  # Smaller group, step 2

    def test_case_4(self):
        self.assertEqual(josephus(10, 5), 3)  # Larger group, step 5

    def test_case_5(self):
        self.assertEqual(josephus(6, 1), 6)  # Eliminate every 1st person

    def test_case_6(self):
        self.assertEqual(josephus(8, 4), 6)  # Step 4 in a group of 8

    def test_case_7(self):
        self.assertEqual(josephus(12, 7), 12)  # Larger group, arbitrary step
if __name__ == '__main__':
    unittest.main()