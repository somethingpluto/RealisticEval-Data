import unittest


class TestWordFilterCounter(unittest.TestCase):

    def test_case1(self):
        text = "go to the school.go to the park."
        filter_words = ["go", "to", "the", "school", "park", "play"]
        expected_output = {
            "go": 2,
            "to": 2,
            "the": 2,
            "school": 1,
            "park": 1,
            "play": 0
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)

    def test_case2(self):
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

    def test_case3(self):
        text = "I will not go to the school's park."
        filter_words = ["I", "will", "not", "go", "to", "the", "school's", "park"]
        expected_output = {
            "I": 1,
            "will": 1,
            "not": 1,
            "go": 1,
            "to": 1,
            "the": 1,
            "school's": 1,
            "park": 1,
        }
        self.assertEqual(word_filter_counter(text, filter_words), expected_output)
