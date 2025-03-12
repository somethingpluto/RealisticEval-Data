from typing import Union, List, Dict, Optional

def get_object_by_id(id: Union[str, int], obj_list: List[Dict]) -> Optional[Dict]:
    for obj in obj_list:
        if 'id' in obj and obj['id'] == id:
            return obj
    return None
import unittest


class TestGetObjectById(unittest.TestCase):

    def test_should_return_object_with_matching_id(self):
        obj_list = [
            {'id': 1, 'name': 'Object 1'},
            {'id': 2, 'name': 'Object 2'},
            {'id': 3, 'name': 'Object 3'}
        ]
        result = get_object_by_id(2, obj_list)
        self.assertEqual(result, {'id': 2, 'name': 'Object 2'})

    def test_should_return_none_if_no_object_with_matching_id(self):
        obj_list = [
            {'id': 1, 'name': 'Object 1'},
            {'id': 2, 'name': 'Object 2'},
            {'id': 3, 'name': 'Object 3'}
        ]
        result = get_object_by_id(4, obj_list)
        self.assertIsNone(result)

    def test_should_return_none_if_list_is_empty(self):
        obj_list = []
        result = get_object_by_id(1, obj_list)
        self.assertIsNone(result)

    def test_should_return_none_if_objects_do_not_have_id_property(self):
        obj_list = [
            {'name': 'Object 1'},
            {'name': 'Object 2'},
            {'name': 'Object 3'}
        ]
        result = get_object_by_id(1, obj_list)
        self.assertIsNone(result)

    def test_should_return_correct_object_when_id_is_string(self):
        obj_list = [
            {'id': 'a', 'name': 'Object A'},
            {'id': 'b', 'name': 'Object B'},
            {'id': 'c', 'name': 'Object C'}
        ]
        result = get_object_by_id('b', obj_list)
        self.assertEqual(result, {'id': 'b', 'name': 'Object B'})

if __name__ == '__main__':
    unittest.main()