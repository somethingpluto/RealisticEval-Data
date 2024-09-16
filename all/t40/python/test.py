import unittest


class TestAdjustToCMajor(unittest.TestCase):
    def test_note_already_in_c_major(self):
        self.assertEqual(adjust_to_c_major("C4"), "C4")
        self.assertEqual(adjust_to_c_major("G3"), "G3")

    def test_note_not_in_c_major(self):
        self.assertEqual(adjust_to_c_major("C#4"), "D4")
        self.assertEqual(adjust_to_c_major("F#3"), "G3")

    def test_invalid_note_name(self):
        self.assertEqual(adjust_to_c_major("H2"), "C4")

    def test_edge_case_near_c_major(self):
        self.assertEqual(adjust_to_c_major("B#3"), "C4")
        self.assertEqual(adjust_to_c_major("E#4"), "F4")