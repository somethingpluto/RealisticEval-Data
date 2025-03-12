import { Dictionary, List } from 'typescript-collections';

function dictOfListsToListOfDicts(dictOfLists: Dictionary<any, List<any>>): Dictionary<string, any> {
  const keys = dictOfLists.keys();
  const firstListLength = dictOfLists.getValue(keys.first()).size();

  if (!keys.every(key => dictOfLists.getValue(key).size() === firstListLength)) {
    throw new Error('All lists must be of the same length.');
  }

  const resultDict = new Dictionary<string, any>();

  for (let i = 0; i < firstListLength; i++) {
    const itemDict: { [key: string]: any } = {};
    keys.forEach(key => {
      itemDict[key] = dictOfLists.getValue(key).get(i);
    });
    resultDict.setValue(i.toString(), itemDict);
  }

  return resultDict;
}
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
