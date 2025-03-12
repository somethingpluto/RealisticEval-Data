from typing import Optional, Dict, Any
import copy

def deep_merge_objects(obj1: Dict[str, Any], obj2: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Deeply merges two objects.

    If properties are objects in both objects, they are recursively merged.
    If a property exists in both objects but is not an object, the value from obj1 is used.

    Args:
        obj1(Dict[str, Any]): The first object to merge.
        obj2(Optional[Dict[str, Any]]): The second object to merge, which can be None.

    Returns:
        Dict[str, Any]: A new object that is the result of the merge.
    """
    result = copy.deepcopy(obj1)

    if obj2 is not None:
        for key, value in obj2.items():
            if key in obj1 and isinstance(obj1[key], dict) and isinstance(value, dict):
                result[key] = deep_merge_objects(obj1[key], value)
            elif key in obj2 and key not in obj1:
                result[key] = value

    return result
import unittest


class TestDeepMergeObjects(unittest.TestCase):

    def test_handles_null_values_in_obj2(self):
        obj1 = {'a': 1, 'b': 2}
        obj2 = None
        result = deep_merge_objects(obj1, obj2)
        self.assertEqual(result, obj1)  # Should return obj1

    def test_handles_undefined_values_in_obj2(self):
        obj1 = {'a': 1, 'b': 2}
        obj2 = None  # Python's equivalent of undefined is None
        result = deep_merge_objects(obj1, obj2)
        self.assertEqual(result, obj1)  # Should return obj1

    def test_merges_deeply_nested_objects(self):
        obj1 = {'a': {'b': {'c': 1}}, 'd': 2}
        obj2 = {'a': {'b': {'d': 3}}, 'e': 4}
        result = deep_merge_objects(obj1, obj2)
        self.assertEqual(result, {
            'a': {
                'b': {
                    'c': 1
                }
            },
            'd': 2
        })

    def test_does_not_merge_arrays_but_takes_them_from_obj1(self):
        obj1 = {'a': [1, 2, 3]}
        obj2 = {'a': [4, 5]}
        result = deep_merge_objects(obj1, obj2)
        self.assertEqual(result, {'a': [1, 2, 3]})  # Should keep array from obj1
if __name__ == '__main__':
    unittest.main()