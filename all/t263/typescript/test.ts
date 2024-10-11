describe('MatrixTraversal', () => {
    it('should traverse a 3x3 matrix in spiral order', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ];
        const expectedOutput = [1, 2, 3, 6, 9, 8, 7, 4, 5];
        // Assuming the function is implemented and available as 'spiralTraverse'
        const result = spiralTraverse(matrix);
        expect(result).toEqual(expectedOutput);
    });

    it('should handle an empty matrix', () => {
        const matrix: number[][] = [];
        const expectedOutput: number[] = [];
        const result = spiralTraverse(matrix);
        expect(result).toEqual(expectedOutput);
    });

    it('should handle a single-element matrix', () => {
        const matrix = [[7]];
        const expectedOutput = [7];
        const result = spiralTraverse(matrix);
        expect(result).toEqual(expectedOutput);
    });
});