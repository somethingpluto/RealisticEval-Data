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