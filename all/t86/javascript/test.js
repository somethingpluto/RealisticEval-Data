describe('Bresenham Line Algorithm', () => {
    it('should generate horizontal line correctly', () => {
        expect(bresenhamLine(1, 5, 5, 5)).toEqual([
            [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]
        ]);
    });

    it('should generate vertical line correctly', () => {
        expect(bresenhamLine(3, 2, 3, 6)).toEqual([
            [3, 2], [3, 3], [3, 4], [3, 5], [3, 6]
        ]);
    });

    it('should generate diagonal line correctly', () => {
        expect(bresenhamLine(2, 2, 6, 6)).toEqual([
            [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]
        ]);
    });

    it('should generate steep slope line correctly', () => {
        expect(bresenhamLine(1, 1, 4, 6)).toEqual([
            [1, 1], [2, 2], [2, 3], [3, 4], [3, 5], [4, 6]
        ]);
    });

    it('should generate negative slope line correctly', () => {
        expect(bresenhamLine(5, 1, 1, 5)).toEqual([
            [5, 1], [4, 2], [3, 3], [2, 4], [1, 5]
        ]);
    });
});