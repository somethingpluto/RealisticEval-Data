describe('bresenhamLine', () => {
    it('should return an array of points for a vertical line', () => {
        const result = bresenhamLine(0, 0, 0, 3);
        expect(result).toEqual([[0, 0], [0, 1], [0, 2], [0, 3]]);
    });

    it('should return an array of points for a horizontal line', () => {
        const result = bresenhamLine(0, 0, 3, 0);
        expect(result).toEqual([[0, 0], [1, 0], [2, 0], [3, 0]]);
    });

    it('should return an array of points for a diagonal line', () => {
        const result = bresenhamLine(0, 0, 3, 3);
        expect(result).toEqual([[0, 0], [1, 1], [2, 2], [3, 3]]);
    });
});