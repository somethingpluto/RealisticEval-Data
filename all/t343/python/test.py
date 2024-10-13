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
