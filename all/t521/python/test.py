import unittest


class TestWordFilterCounter(unittest.TestCase):

    def test_basic_functionality(self):
        text = "I'll go to the school. I'll go to the park."
        filter_words = ["I'll", "go", "to", "the", "school", "park", "play"]
        expected_output = {
            "I'll": 2,
            "go": 2,
            "to": 2,
            "the": 2,
            "school": 1,
            "park": 1,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

    def test_case_insensitivity(self):
        text = "i'll Go To The School. I'll Go to the park."
        filter_words = ["I'll", "go", "to", "the", "school", "park", "play"]
        expected_output = {
            "I'll": 2,
            "go": 2,
            "to": 2,
            "the": 2,
            "school": 1,
            "park": 1,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

    def test_no_occurrences(self):
        text = "This is a completely different sentence."
        filter_words = ["I'll", "go", "to", "the", "school", "park", "play"]
        expected_output = {
            "I'll": 0,
            "go": 0,
            "to": 0,
            "the": 0,
            "school": 0,
            "park": 0,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)


    def test_filter_words_with_special_characters(self):
        text = "I won't go to the school's park."
        filter_words = ["I'll", "go", "to", "the", "school's", "park", "play"]
        expected_output = {
            "I'll": 0,
            "go": 1,
            "to": 1,
            "the": 1,
            "school's": 1,
            "park": 1,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)
