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