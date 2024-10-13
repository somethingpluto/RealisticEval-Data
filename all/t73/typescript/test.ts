describe('TestDictOfListsToListOfDicts', () => {
  it('test_standard_conversion', () => {
      const dictOfLists = {
          "name": ["Alice", "Bob", "Charlie"],
          "age": [25, 30, 35],
          "city": ["New York", "Los Angeles", "Chicago"]
      };
      const expectedResult = [
          { name: 'Alice', age: 25, city: 'New York' },
          { name: 'Bob', age: 30, city: 'Los Angeles' },
          { name: 'Charlie', age: 35, city: 'Chicago' }
      ];
      const result = dictOfListsToListOfDicts(dictOfLists);
      expect(result).toEqual(expectedResult);
  });

  it('test_empty_lists', () => {
      const dictOfLists = {
          "name": [],
          "age": [],
          "city": []
      };
      const expectedResult = [];
      const result = dictOfListsToListOfDicts(dictOfLists);
      expect(result).toEqual(expectedResult);
  });

  it('test_single_element_lists', () => {
      const dictOfLists = {
          "name": ["Alice"],
          "age": [25],
          "city": ["New York"]
      };
      const expectedResult = [
          { name: 'Alice', age: 25, city: 'New York' }
      ];
      const result = dictOfListsToListOfDicts(dictOfLists);
      expect(result).toEqual(expectedResult);
  });
});