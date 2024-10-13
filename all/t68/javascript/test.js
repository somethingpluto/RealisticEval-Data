describe('TestDivideList', () => {
    it('should handle even division', () => {
        const lst = [1, 2, 3, 4, 5, 6];
        const n = 3;
        const expected = [[1, 2], [3, 4], [5, 6]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle uneven division', () => {
        const lst = [1, 2, 3, 4, 5, 6, 7];
        const n = 3;
        const expected = [[1, 2, 3], [4, 5], [6, 7]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle more parts than items', () => {
        const lst = [1, 2, 3];
        const n = 5;
        const expected = [[1], [2], [3], [], []];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle a single element', () => {
        const lst = [1];
        const n = 1;
        const expected = [[1]];
        expect(divideList(lst, n)).toEqual(expected);
    });

    it('should handle an empty list', () => {
        const lst = [];
        const n = 3;
        const expected = [[], [], []];
        expect(divideList(lst, n)).toEqual(expected);
    });
});