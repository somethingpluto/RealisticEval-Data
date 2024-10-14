import unittest


class TestSortByTimestamp(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_by_timestamp([]), [])

    def test_single_element_array(self):
        single_element_array = [{'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}]
        self.assertEqual(sort_by_timestamp(single_element_array), [{'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}])

    def test_sort_multiple_elements(self):
        test_data = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 1, 'timestamp': "2021-07-03T12:00:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"}
        ]
        expected = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"},
            {'id': 1, 'timestamp': "2021-07-03T12:00:00Z"}
        ]
        self.assertEqual(sort_by_timestamp(test_data), expected)

    def test_already_sorted_array(self):
        sorted_array = [
            {'id': 1, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "2021-07-02T15:30:00Z"},
            {'id': 3, 'timestamp': "2021-07-03T12:00:00Z"}
        ]
        self.assertEqual(sort_by_timestamp(sorted_array), sorted_array)

    def test_mixed_format_timestamps(self):
        mixed_formats = [
            {'id': 1, 'timestamp': "2021/07/03 12:00:00"},
            {'id': 2, 'timestamp': "July 2, 2021 15:30:00"},
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"}
        ]
        expected = [
            {'id': 3, 'timestamp': "2021-07-01T09:45:00Z"},
            {'id': 2, 'timestamp': "July 2, 2021 15:30:00"},
            {'id': 1, 'timestamp': "2021/07/03 12:00:00"}
        ]
        self.assertEqual(sort_by_timestamp(mixed_formats), expected)
