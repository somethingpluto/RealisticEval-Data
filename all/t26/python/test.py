import unittest


class TestConvertToCommaSeparated(unittest.TestCase):
    def test_basic_separators(self):
        self.assertEqual(convert_to_comma_separated("apple;banana*orange/mango"), "apple,banana,orange,mango",
                         "Failed to convert basic separators.")

    def test_mixed_separators(self):
        self.assertEqual(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi"), "grapes,lemon,melon,kiwi,litchi",
                         "Failed to convert mixed separators in a string.")

    def test_no_separators(self):
        self.assertEqual(convert_to_comma_separated("watermelon"), "watermelon",
                         "Failed when no separators are present.")

    def test_repeated_separators(self):
        self.assertEqual(convert_to_comma_separated("pear;;apple**banana//orange"), "pear,,apple,,banana,,orange",
                         "Failed to handle repeated separators correctly.")

    def test_multiple_types(self):
        self.assertEqual(convert_to_comma_separated("papaya;guava*fig/tomato:carrot-lettuce"),
                         "papaya,guava,fig,tomato,carrot,lettuce",
                         "Failed to handle multiple types of separators.")
