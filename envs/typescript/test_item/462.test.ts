import { Matrix } from './Matrix';

function spiralOrder(matrix: Matrix): number[] {
  const result: number[] = [];
  let top = 0, bottom = matrix.rows - 1;
  let left = 0, right = matrix.cols - 1;

  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      result.push(matrix.get(top, i));
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      result.push(matrix.get(i, right));
    }
    right--;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix.get(bottom, i));
      }
      bottom--;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix.get(i, left));
      }
      left++;
    }
  }

  return result;
}
describe('Test Spiral Order', () => {
    it('should handle an empty matrix', () => {
        expect(spiralOrder([])).toEqual([]);
    });

    it('should handle a single row matrix', () => {
        expect(spiralOrder([[1, 2, 3]])).toEqual([1, 2, 3]);
    });

    it('should handle a single column matrix', () => {
        expect(spiralOrder([[1], [2], [3]])).toEqual([1, 2, 3]);
    });

    it('should handle a square matrix', () => {
        expect(spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
    });

    it('should handle a rectangular matrix', () => {
        expect(spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ])).toEqual([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]);
    });
});
