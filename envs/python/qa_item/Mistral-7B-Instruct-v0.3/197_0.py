def josephus(n: int, k: int) -> int:
    if n <= 0 or k <= 0:
        raise ValueError("Both n and k must be positive integers.")

    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)

    return people[0]
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