describe('minWindow', () => {
    it('test with a normal case where the minimum window exists', () => {
        const s = "ADOBECODEBANC";
        const t = "ABC";
        const expectedOutput = "BANC";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test where no window can satisfy the condition', () => {
        const s = "A";
        const t = "AA";
        const expectedOutput = "";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test with an empty input string s', () => {
        const s = "";
        const t = "ABC";
        const expectedOutput = "";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test with multiple valid windows to ensure the smallest one is returned', () => {
        const s = "AA";
        const t = "AA";
        const expectedOutput = "AA";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });
});