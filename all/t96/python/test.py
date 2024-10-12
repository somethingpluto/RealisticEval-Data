class TestChangedClef(unittest.TestCase):

    def test_default_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = changed_clef(abc)
        expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_specific_clef_insertion(self):
        abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n"
        result = changed_clef(abc, "treble")
        expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n"
        self.assertEqual(result, expected)

    def test_no_newline_after_key_signature(self):
        abc = "X:1\nT:Test Tune\nK:C"
        result = changed_clef(abc, "alto")
        expected = "X:1\nT:Test Tune\nK:C clef=alto"
        self.assertEqual(result, expected)

    def test_no_key_signature_found(self):
        abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n"
        result = changed_clef(abc, "tenor")
        self.assertEqual(result, abc)  # Expect the original string to be returned unchanged

    def test_multiple_key_signatures(self):
        abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n"
        result = changed_clef(abc, "baritone")
        expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n"
        self.assertEqual(result, expected)
