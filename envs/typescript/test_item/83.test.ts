// At the start of your TypeScript file
import { rotateListElements } from './rotateListElements';

// ... (rest of your TypeScript code)

// Jest unit tests for rotateListElements function
describe('rotateListElements', () => {
  it('rotates an empty array', () => {
    expect(rotateListElements([])).toEqual([]);
  });

  it('rotates a single-element array', () => {
    expect(rotateListElements([1])).toEqual([1]);
  });

  it('rotates an array with multiple elements', () => {
    expect(rotateListElements([1, 2, 3, 4])).toEqual([2, 3, 4, 1]);
  });

  it('rotates an array with negative numbers', () => {
    expect(rotateListElements([-1, -2, -3])).toEqual([-2, -3, -1]);
  });

  it('rotates an array with zeros', () => {
    expect(rotateListElements([0, 0, 0])).toEqual([0, 0, 0]);
  });
});
describe('TestRotateListElements', () => {
    it('should rotate the list elements correctly', () => {
        expect(rotateListElements([1, 2, 3, 4])).toEqual([2, 3, 4, 1]);
    });

    it('single element list should remain unchanged', () => {
        expect(rotateListElements([10])).toEqual([10]);
    });

    it('empty list should remain unchanged', () => {
        expect(rotateListElements([])).toEqual([]);
    });

    it('should correctly rotate a two-element list', () => {
        expect(rotateListElements([5, 9])).toEqual([9, 5]);
    });

    it('should correctly rotate a large list', () => {
        const largeList = Array.from({ length: 1000 }, (_, i) => i + 1);
        const rotatedList = rotateListElements(largeList);
        expect(rotatedList).toEqual(Array.from({ length: 999 }, (_, i) => i + 2).concat([1]));
    });
});
