
from typing import List

def create_circle_of_fifths(starting_note: str) -> List[str]:
    """
    Generates a cyclic tone sequence of five degrees of length 12 starting with the specified starting note.

    Args:
        starting_note (str): The musical note to start the Circle of Fifths from (e.g., "C").

    Returns:
        List[str]: A list representing the Circle of Fifths.
    """
    # Convert the starting note to a tuple of the note and its BCD value
    starting_note_tuple = (starting_note,)
    BCD_values = [int(c) for c in starting_note_tuple]

    # Generate the cyclic tone sequence
    circle_of_fifths = []
    for i in range(12):
        # Calculate the BCD value for the next note in the sequence
        BCD_value = BCD_values[i % len(BCD_values)]
        # Add the note and its BCD value to the list
        circle_of_fifths.append("{} {}".format(BCD_value, starting_note))

    return circle_of_fifths

import unittest


class TestCreateCircleOfFifths(unittest.TestCase):
    def test_should_return_12_notes_in_the_circle(self):
        result = create_circle_of_fifths('C')
        self.assertEqual(len(result), 12)

    def test_should_start_with_the_given_starting_note(self):
        starting_note = 'G'
        result = create_circle_of_fifths(starting_note)
        self.assertEqual(result[0], starting_note)

    def test_should_correctly_generate_the_circle_of_fifths_starting_from_C(self):
        result = create_circle_of_fifths('C')
        expected_circle = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#']
        self.assertEqual(result, expected_circle)

    def test_should_correctly_generate_the_circle_of_fifths_starting_from_G(self):
        result = create_circle_of_fifths('G')
        expected_circle = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#']
        self.assertEqual(result, expected_circle)

    def test_should_correctly_generate_the_circle_of_fifths_starting_from_F(self):
        result = create_circle_of_fifths('F')
        expected_circle = ['F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']
        self.assertEqual(result, expected_circle)

if __name__ == '__main__':
    unittest.main()