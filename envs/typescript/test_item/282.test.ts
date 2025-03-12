import { isArray } from 'lodash';

function flattenArray(multiDimArray: any[]): number[] | any[] {
    let flatArray: any[] = [];
    multiDimArray.forEach(element => {
        if (isArray(element)) {
            flatArray = flatArray.concat(flattenArray(element));
        } else {
            flatArray.push(element);
        }
    });
    return flatArray;
}
describe('TestFlattenArray', () => {
  it('testDeeplyNestedArray', () => {
      const nestedArray = [1, [2, [3, [4, [5]]]]];
      const expectedResult = [1, 2, 3, 4, 5];
      expect(flattenArray(nestedArray)).toEqual(expectedResult);
  });

  it('testMixedTypes', () => {
      const mixedArray = ["a", ["b", 2, [true, [3.14]]], false];
      const expectedResult = ["a", "b", 2, true, 3.14, false];
      expect(flattenArray(mixedArray)).toEqual(expectedResult);
  });

  it('testEmptyArray', () => {
      const emptyArray: any[] = [];
      const expectedResult: any[] = [];
      expect(flattenArray(emptyArray)).toEqual(expectedResult);
  });

  it('testArrayWithEmptySubarrays', () => {
      const complexArray = [1, [], [2, [], 3], [4, [5, [], 6], 7], []];
      const expectedResult = [1, 2, 3, 4, 5, 6, 7];
      expect(flattenArray(complexArray)).toEqual(expectedResult);
  });

  it('testNoNestedArray', () => {
      const flatArray = [1, 2, 3, 4, 5];
      const expectedResult = [1, 2, 3, 4, 5];
      expect(flattenArray(flatArray)).toEqual(expectedResult);
  });
});
