from typing import List, Tuple
import re

def insert_clef(abc: str, clef: str = "bass") -> str:
    def get_tone_line_indices(abc: str) -> Tuple[int, int]:
        tone_line_pattern = r'K:'
        tone_line_matches = re.finditer(tone_line_pattern, abc)
        tone_line_indices = [match.start() for match in tone_line_matches]
        return tone_line_indices[0] if tone_line_indices else 0, tone_line_indices[0] + len("K:")

    def insert_clef_after_tone_line(abc: str, clef: str) -> str:
        tone_start, tone_end = get_tone_line_indices(abc)
        return abc[:tone_end] + f" clef={clef} " + abc[tone_end:]

    return insert_clef_after_tone_line(abc, clef)
import unittest


class TestChangedClef(unittest.TestCase):

    def test_default_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = insert_clef(abc)
        expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_specific_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = insert_clef(abc, "treble")
        expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_no_newline_after_key_signature(self):
        abc = "X:1\nT:Test Tune\nK:C"
        result = insert_clef(abc, "alto")
        expected = "X:1\nT:Test Tune\nK:C clef=alto"
        self.assertEqual(result, expected)

    def test_no_key_signature_found(self):
        abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n"
        result = insert_clef(abc, "tenor")
        self.assertEqual(result, abc)  # Expect the original string to be returned unchanged

    def test_multiple_key_signatures(self):
        abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n"
        result = insert_clef(abc, "baritone")
        expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()