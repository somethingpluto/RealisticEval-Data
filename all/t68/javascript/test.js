describe('divideList', () => {
    it('should divide a list evenly into n parts', () => {
        const inputList = [1, 2, 3, 4, 5];
        const n = 2;
        const expectedResult = [[1, 2], [3, 4, 5]];
        expect(divideList(inputList, n)).toEqual(expectedResult);
    });

    it('should handle empty list', () => {
        const inputList = [];
        const n = 3;
        const expectedResult = [];
        expect(divideList(inputList, n)).toEqual(expectedResult);
    });

    it('should handle list with less elements than n', () => {
        const inputList = [1, 2];
        const n = 5;
        const expectedResult = [[1, 2], [], [], []];
        expect(divideList(inputList, n)).toEqual(expectedResult);
    });
});