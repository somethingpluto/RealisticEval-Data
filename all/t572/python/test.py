import unittest


class Item:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Item(id='{self.id}', name='{self.name}')"
class TestMergeOrUpdate(unittest.TestCase):

    def test_merges_two_arrays_with_unique_items(self):
        arr1 = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        arr2 = [Item('3', 'Item 3'), Item('4', 'Item 4')]
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Item 1'), Item('2', 'Item 2'), Item('3', 'Item 3'), Item('4', 'Item 4')]
        self.assertListEqual(result, expected)

    def test_updates_existing_items_when_ids_match(self):
        arr1 = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        arr2 = [Item('2', 'Updated Item 2'), Item('3', 'Item 3')]
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Item 1'), Item('2', 'Updated Item 2'), Item('3', 'Item 3')]
        self.assertListEqual(result, expected)

    def test_handles_empty_arrays(self):
        arr1 = []
        arr2 = []
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = []
        self.assertListEqual(result, expected)

    def test_merges_with_an_empty_first_array(self):
        arr1 = []
        arr2 = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        self.assertListEqual(result, expected)

    def test_merges_with_an_empty_second_array(self):
        arr1 = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        arr2 = []
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        self.assertListEqual(result, expected)

    def test_handles_duplicate_ids_in_the_first_array(self):
        arr1 = [Item('1', 'Item 1'), Item('1', 'Duplicate Item 1')]  # Duplicate ID
        arr2 = [Item('2', 'Item 2')]
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Duplicate Item 1'), Item('2', 'Item 2')]  # Last occurrence takes precedence
        self.assertListEqual(result, expected)

    def test_handles_duplicate_ids_in_the_second_array(self):
        arr1 = [Item('1', 'Item 1')]
        arr2 = [Item('2', 'Item 2'), Item('2', 'Duplicate Item 2')]  # Duplicate ID
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'Item 1'), Item('2', 'Duplicate Item 2')]  # Last occurrence takes precedence
        self.assertListEqual(result, expected)

    def test_merges_arrays_with_mixed_unique_and_duplicate_ids(self):
        arr1 = [Item('1', 'Item 1'), Item('2', 'Item 2')]
        arr2 = [Item('2', 'Updated Item 2'), Item('3', 'Item 3'), Item('1', 'New Item 1')]  # Updated item with same ID
        result = mergeOrUpdate(arr1, arr2, lambda item: item.id)
        expected = [Item('1', 'New Item 1'), Item('2', 'Updated Item 2'), Item('3', 'Item 3')]
        self.assertListEqual(result, expected)