describe('TestDictOfListsToListOfDicts', () => {
  describe('test_standard_conversion', () => {
      it('should correctly convert a dictionary of lists into a list of dictionaries with equal length lists', () => {
          const dictOfLists = {
              name: ['Alice', 'Bob', 'Charlie'],
              age: [25, 30, 35],
              city: ['New York', 'Los Angeles', 'Chicago']
          };
          const expectedResult = [
              { name: 'Alice', age: 25, city: 'New York' },
              { name: 'Bob', age: 30, city: 'Los Angeles' },
              { name: 'Charlie', age: 35, city: 'Chicago' }
          ];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });

  describe('test_empty_lists', () => {
      it('should handle empty lists correctly', () => {
          const dictOfLists = {
              name: [],
              age: [],
              city: []
          };
          const expectedResult = [];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });

  describe('test_single_element_lists', () => {
      it('should correctly convert a dictionary of single-element lists into a list of dictionaries', () => {
          const dictOfLists = {
              name: ['Alice'],
              age: [25],
              city: ['New York']
          };
          const expectedResult = [
              { name: 'Alice', age: 25, city: 'New York' }
          ];
          const result = dictOfListsToListOfDicts(dictOfLists);
          expect(result).toEqual(expectedResult);
      });
  });
});