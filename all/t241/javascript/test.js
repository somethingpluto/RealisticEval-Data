describe('getMinSeqNumAndDistance', () => {
    it('should find the minimum distance between two words', () => {
        const filePath = path.join(__dirname, 'test.txt');
        const result = getMinSeqNumAndDistance(filePath, 'apple', 'banana');
        expect(result).toEqual([2, 3]);
    });

    it('should handle case where one word is not found', () => {
        const filePath = path.join(__dirname, 'test.txt');
        const result = getMinSeqNumAndDistance(filePath, 'apple', 'orange');
        expect(result).toEqual([null, Infinity]);
    });

    it('should handle case where both words are not found', () => {
        const filePath = path.join(__dirname, 'test.txt');
        const result = getMinSeqNumAndDistance(filePath, 'grape', 'kiwi');
        expect(result).toEqual([null, Infinity]);
    });
});