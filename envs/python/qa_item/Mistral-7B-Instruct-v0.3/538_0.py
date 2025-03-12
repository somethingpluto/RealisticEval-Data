from operator import itemgetter

def sort_by_field(array, field, ascending=True):
    """
    Sorts a list of dictionaries alphabetically based on a specified field.

    :param array: List of dictionaries to sort.
    :param field: The field of the dictionaries to sort by.
    :param ascending: If True, sort in ascending order; if False, sort in descending order.
    :return: The sorted list of dictionaries.
    """
    sorted_array = sorted(array, key=itemgetter(field), reverse=not ascending)
    return sorted_array
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

if __name__ == '__main__':
    unittest.main()