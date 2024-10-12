class TestSortByField(unittest.TestCase):

    def setUp(self):
        self.data = [
            {'name': 'John', 'age': 25},
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 28},
        ]

    def test_sort_by_name_ascending(self):
        sorted_data = sort_by_field(self.data, 'name', True)
        expected = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 28},
            {'name': 'John', 'age': 25},
        ]
        self.assertEqual(sorted_data, expected)

    def test_sort_by_name_descending(self):
        sorted_data = sort_by_field(self.data, 'name', False)
        expected = [
            {'name': 'John', 'age': 25},
            {'name': 'Charlie', 'age': 28},
            {'name': 'Bob', 'age': 22},
            {'name': 'Alice', 'age': 30},
        ]
        self.assertEqual(sorted_data, expected)

    def test_sort_by_age_ascending(self):
        sorted_data = sort_by_field(self.data, 'age', True)
        expected = [
            {'name': 'Bob', 'age': 22},
            {'name': 'John', 'age': 25},
            {'name': 'Charlie', 'age': 28},
            {'name': 'Alice', 'age': 30},
        ]
        self.assertEqual(sorted_data, expected)

    def test_sort_by_age_descending(self):
        sorted_data = sort_by_field(self.data, 'age', False)
        expected = [
            {'name': 'Alice', 'age': 30},
            {'name': 'Charlie', 'age': 28},
            {'name': 'John', 'age': 25},
            {'name': 'Bob', 'age': 22},
        ]
        self.assertEqual(sorted_data, expected)
