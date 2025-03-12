def merge_objects(obj1: dict, obj2: dict) -> dict:
    """
    Merges two dictionaries into one, with properties from the second dictionary
    potentially overwriting those from the first if there are conflicts.

    Args:
        obj1 (dict): The first dictionary.
        obj2 (dict): The second dictionary.

    Returns:
        dict: The resulting dictionary after merging.
    """
    return {**obj1, **obj2}
import unittest

class TestMergeObjects(unittest.TestCase):
    
    def test_correctly_merges_two_objects_with_non_conflicting_keys(self):
        obj1 = {'name': "Alice"}
        obj2 = {'age': 30}
        expected = {'name': "Alice", 'age': 30}
        self.assertEqual(merge_objects(obj1, obj2), expected)

    def test_properties_from_second_object_overwrite_properties_from_first(self):
        obj1 = {'name': "Alice", 'age': 25}
        obj2 = {'age': 30}
        expected = {'name': "Alice", 'age': 30}
        self.assertEqual(merge_objects(obj1, obj2), expected)

    def test_merges_objects_with_nested_structures_correctly(self):
        obj1 = {'user': {'name': "Alice", 'age': 25}}
        obj2 = {'user': {'age': 30}}
        expected = {'user': {'age': 30}}  # Note: obj2 does not merge deeply
        self.assertEqual(merge_objects(obj1, obj2), expected)
if __name__ == '__main__':
    unittest.main()