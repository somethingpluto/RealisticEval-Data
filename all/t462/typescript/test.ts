import { describe, it, expect } from '@jest/globals';

function spiralOrder(matrix: number[][]): number[] {
    if (matrix.length === 0) return [];

    const result: number[] = [];
    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        // Traverse from left to right along the top row
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top++;

        // Traverse downwards along the right column
        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right--;

        // Traverse from right to left along the bottom row
        if (top <= bottom) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }

        // Traverse upwards along the left column
        if (left <= right) {
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left++;
        }
    }

    return result;
}

describe('spiralOrder', () => {
    it('should return the elements of a 3x3 matrix in spiral order', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ];
        expect(spiralOrder(matrix)).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
    });

    it('should return the elements of a 2x3 matrix in spiral order', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ];
        expect(spiralOrder(matrix)).toEqual([1, 2, 3, 6, 5, 4]);
    });

    it('should return the elements of a 3x2 matrix in spiral order', () => {
        const matrix = [
            [1, 2],
            [3, 4],
            [5, 6]
        ];
        expect(spiralOrder(matrix)).toEqual([1, 2, 4, 6, 5, 3]);
    });

    it('should return an empty array for an empty matrix', () => {
        const matrix: number[][] = [];
        expect(spiralOrder(matrix)).toEqual([]);
    });
});