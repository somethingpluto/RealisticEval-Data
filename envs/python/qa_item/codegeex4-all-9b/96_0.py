def insert_clef(abc: str, clef: str = "bass") -> str:
    """
    Modify the ABC string by inserting the specified clef (e.g., "clef=bass")
    after the tone line (K:), or "bass" if no clef is specified.

    Args:
        abc (str): The ABC notation string.
        clef (str): The clef to set (default is "bass").

    Returns:
        str: The updated ABC notation string with the new clef.
    """
    lines = abc.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('K:'):
            lines.insert(i + 1, f'clef={clef}')
            break
    return '\n'.join(lines)
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