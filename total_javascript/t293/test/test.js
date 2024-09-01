describe('reorderData', () => {
    test('sorts data correctly for basic inputs', () => {
        const scores = [3, 1, 2];
        const names = ['Image3', 'Image1', 'Image2'];
        const ids = [103, 101, 102];
        const expected = {
            resultScores: [1, 2, 3],
            resultNames: ['Image1', 'Image2', 'Image3'],
            resultIDs: [101, 102, 103]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('sorts data correctly with mixed scores', () => {
        const scores = [5, 1, 3, 5, 2];
        const names = ['Image5', 'Image1', 'Image3', 'Image6', 'Image2'];
        const ids = [105, 101, 103, 106, 102];
        const expected = {
            resultScores: [1, 2, 3, 5, 5],
            resultNames: ['Image1', 'Image2', 'Image3', 'Image5', 'Image6'],
            resultIDs: [101, 102, 103, 105, 106]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('handles duplicate scores', () => {
        const scores = [2, 2, 1];
        const names = ['Image2', 'Image3', 'Image1'];
        const ids = [102, 103, 101];
        const expected = {
            resultScores: [1, 2, 2],
            resultNames: ['Image1', 'Image2', 'Image3'],
            resultIDs: [101, 102, 103]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('handles empty arrays', () => {
        const scores = [];
        const names = [];
        const ids = [];
        const expected = {
            resultScores: [],
            resultNames: [],
            resultIDs: []
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

});