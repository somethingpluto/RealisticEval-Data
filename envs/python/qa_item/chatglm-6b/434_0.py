
from typing import List

def get_max_people(people: List[int], status: List[str]) -> int:
    """
    Amazon is organizing a farewell party for its interns at a large party hall! There are q events in the form "+x" and "-x" that denote person x has entered or left the party, respectively.   Find the maximum number of people at any time at the party.Return -1 if the series of events is not possible.

    Args:
        people(List[int]): people array
        status(List[str]): people action array

    Returns:
        int: the maximum number of people at any time at the party or -1 is series of events is not possible
    """
    # Iterate through the people array and status array
    for i in range(len(people)):
        # Check if the current person has already entered or left the party
        if people[i] == 0 or people[i] == 1:
            # If they have, return the maximum number of people
            return max(people[i] + 1, people[i] - 1)
        # If they haven't, add the current person to the people array and status array
        people[i] += 1
        status[i] += people[i]
    # If the maximum number of people is found, return -1
    return -1

import unittest


class TestGetMaxPeople(unittest.TestCase):

    def test_case_1(self):
        people = [1, 2, 3]
        status = ['+', '+', '-']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_2(self):
        people = [1, 2, 1]
        status = ['+', '-', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_3(self):
        people = [1, 2, 1]
        status = ['+', '+', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)

    def test_case_4(self):
        people = [1, 2, 1]
        status = ['+', '+', '+']
        expected = -1
        self.assertEqual(get_max_people(people, status), expected)
if __name__ == '__main__':
    unittest.main()