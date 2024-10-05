import unittest


class TestAdjustToCMajor(unittest.TestCase):
    def test_normal_note(self):
        self.assertEqual(adjust_to_c_major('C'), 'C')
        self.assertEqual(adjust_to_c_major('G'), 'G')

    def test_sharp_note(self):
        self.assertEqual(adjust_to_c_major('C#'), 'D')
        self.assertEqual(adjust_to_c_major('F#'), 'G')

    def test_flat_note(self):
        self.assertEqual(adjust_to_c_major('Db'), 'C')
        self.assertEqual(adjust_to_c_major('Eb'), 'E')
        self.assertEqual(adjust_to_c_major('Gb'), 'G')

    def test_edge_case_high_octave(self):
        self.assertEqual(adjust_to_c_major('C8'), 'C')
        self.assertEqual(adjust_to_c_major('A#5'), 'A')

    def test_edge_case_note_with_spaces(self):
        self.assertEqual(adjust_to_c_major(' Bb '), 'A')
        self.assertEqual(adjust_to_c_major(' G#'), 'G')

    def test_complex_input(self):
        self.assertEqual(adjust_to_c_major('D#3'), 'E')
        self.assertEqual(adjust_to_c_major('Ab2'), 'G')
