describe('Test Pascal Triangle Row', () => {
    it('test row 0', () => {
        expect(pascalTriangleRow(0)).toEqual([1]);
    });

    it('test row 1', () => {
        expect(pascalTriangleRow(1)).toEqual([1, 1]);
    });

    it('test row 2', () => {
        expect(pascalTriangleRow(2)).toEqual([1, 2, 1]);
    });

    it('test row 3', () => {
        expect(pascalTriangleRow(3)).toEqual([1, 3, 3, 1]);
    });

    it('test row 4', () => {
        expect(pascalTriangleRow(4)).toEqual([1, 4, 6, 4, 1]);
    });

    it('test row 5', () => {
        expect(pascalTriangleRow(5)).toEqual([1, 5, 10, 10, 5, 1]);
    });
});