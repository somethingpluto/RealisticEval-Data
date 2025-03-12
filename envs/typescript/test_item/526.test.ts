function minWindow(s: string, t: string): string {
    const charFrequency = new Map<string, number>();
    let required = 0;
    let formed = 0;

    // Count the frequency of each character in t
    for (const char of t) {
        const count = charFrequency.get(char) || 0;
        charFrequency.set(char, count + 1);
        if (count === 0) required++;
    }

    let left = 0;
    let right = 0;
    let windowCounts = new Map<string, number>();
    let minLength = Infinity;
    let minWindow = '';

    while (right < s.length) {
        const char = s[right];
        const count = windowCounts.get(char) || 0;
        windowCounts.set(char, count + 1);

        if (charFrequency.has(char) && windowCounts.get(char) === charFrequency.get(char)) {
            formed++;
        }

        while (left <= right && formed === required) {
            const currentLength = right - left + 1;
            if (currentLength < minLength) {
                minLength = currentLength;
                minWindow = s.substring(left, right + 1);
            }

            const leftChar = s[left];
            windowCounts.set(leftChar, windowCounts.get(leftChar) - 1);
            if (charFrequency.has(leftChar) && windowCounts.get(leftChar) < charFrequency.get(leftChar)) {
                formed--;
            }
            left++;
        }
        right++;
    }

    return minWindow;
}
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
