describe('alignLinesLeft', () => {
    it('should align two lines of equal length', () => {
        const result = alignLinesLeft('hello', 'world');
        expect(result).toEqual(['hello', 'world']);
    });

    it('should align two lines where the first one is shorter', () => {
        const result = alignLinesLeft('hi', 'there');
        expect(result).toEqual(['hi   ', 'there']);
    });

    it('should align two lines where the second one is shorter', () => {
        const result = alignLinesLeft('this is long', 'short');
        expect(result).toEqual(['this is long', 'short   ']);
    });
});