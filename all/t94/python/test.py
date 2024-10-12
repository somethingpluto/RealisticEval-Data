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
