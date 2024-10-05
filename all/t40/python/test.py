import unittest
from music21 import pitch

class TestAdjustToCMajor(unittest.TestCase):
    def test_note_in_c_major(self):
        self.assertEqual(adjust_to_c_major("C4"), "C4")
        self.assertEqual(adjust_to_c_major("E5"), "E5")


    def test_transpose_to_c_major(self):
        # F# should adjust to G (closest in C major)
        self.assertEqual(adjust_to_c_major("F#4"), "G4")
        # Eb should adjust to D or E, depending on direction (choosing the closest)
        self.assertEqual(adjust_to_c_major("Eb4"), "E4")

    def test_invalid_note_name(self):
        # Invalid note input should return C4 as per the fallback in your function
        self.assertEqual(adjust_to_c_major("H2"), "C4")

    def test_extreme_octaves(self):
        # Testing lower and higher octaves
        self.assertEqual(adjust_to_c_major("A0"), "A0")
        self.assertEqual(adjust_to_c_major("G8"), "G8")

    def test_edge_case_note_transitions(self):
        # Edge cases where the note might need to jump over a natural semitone
        self.assertEqual(adjust_to_c_major("B3"), "B3")
        self.assertEqual(adjust_to_c_major("Db4"), "D4")  # Db should adjust to D