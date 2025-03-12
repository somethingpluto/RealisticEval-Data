def compare_objects_depth(obj1: dict, obj2: dict) -> bool:
    def _compare(obj1, obj2, depth=1):
        if not isinstance(obj1, dict) or not isinstance(obj2, dict):
            return False

        if len(obj1)!= len(obj2):
            return False

        for key1, value1 in obj1.items():
            key2 = obj2.get(key1)
            if key2 is None:
                return False

            if not _compare(value1, key2, depth + 1):
                return False

        return True

    return _compare(obj1, obj2)
import unittest


class TestCompareObjectsDepth(unittest.TestCase):

    def test_equal_depth_and_structure(self):
        objA = {'a': {'b': {'c': 1}}, 'd': 2}
        objB = {'a': {'b': {'c': 3}}, 'd': 4}
        self.assertFalse(compare_objects_depth(objA, objB))  # Same structure

    def test_different_structure_missing_key(self):
        objA = {'a': {'b': {'c': 1}}, 'd': 2}
        objC = {'a': {'b': {'c': 3}}, 'e': 4}
        self.assertFalse(compare_objects_depth(objA, objC))  # Different structure

    def test_different_depth(self):
        objA = {'a': {'b': {'c': 1}}, 'd': 2}
        objD = {'a': {'b': 1}, 'd': 2}
        self.assertFalse(compare_objects_depth(objA, objD))  # Different depth

    def test_non_object_inputs(self):
        objA = {'a': {'b': {'c': 1}}, 'd': 2}
        objE = None
        self.assertFalse(compare_objects_depth(objA, objE))  # Non-object input

    def test_different_types(self):
        objA = {'a': {'b': 1}, 'd': 2}
        objF = {'a': {'b': {'c': 3}}, 'd': 4}
        self.assertFalse(compare_objects_depth(objA, objF))  # Different types

    def test_identical_empty_objects(self):
        objG = {}
        objH = {}
        self.assertTrue(compare_objects_depth(objG, objH))  # Both are empty

if __name__ == '__main__':
    unittest.main()