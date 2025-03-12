/**
 * Find the minimum window substring in `s` that contains all characters of `t`.
 *
 * @param {string} s - The input string in which to search for the substring.
 * @param {string} t - The target string whose characters must be included in the substring.
 * @returns {string} The minimum window substring of `s` that contains all characters of `t`.
 *                   Returns an empty string if no such substring exists.
 */
function minWindow(s, t) {
    const targetMap = {};
    const windowMap = {};
    let requiredCount = 0;
    let formedCount = 0;
    let left = 0;
    let right = 0;
    let minLength = Infinity;
    let minWindowStart = 0;

    // Populate the target map with the frequency of each character in `t`
    for (let char of t) {
        if (targetMap[char]) {
            targetMap[char]++;
        } else {
            targetMap[char] = 1;
            requiredCount++;
        }
    }

    // Expand the window by moving the right pointer
    while (right < s.length) {
        const char = s[right];
        if (targetMap[char]) {
            windowMap[char] = (windowMap[char] || 0) + 1;
            if (windowMap[char] === targetMap[char]) {
                formedCount++;
            }
        }

        // Try to contract the window by moving the left pointer
        while (left <= right && formedCount === requiredCount) {
            const currentLength = right - left + 1;
            if (currentLength < minLength) {
                minLength = currentLength;
                minWindowStart = left;
            }

            const leftChar = s[left];
            if (targetMap[leftChar]) {
                windowMap[leftChar]--;
                if (windowMap[leftChar] < targetMap[leftChar]) {
                    formedCount--;
                }
            }
            left++;
        }

        right++;
    }

    return minLength === Infinity ? "" : s.substring(minWindowStart, minWindowStart + minLength);
}
describe('TestMinWindow', () => {
    it('test basic case', () => {
        /** Test with a normal case where the minimum window exists. */
        const s = "ADOBECODEBANC";
        const t = "ABC";
        const expectedOutput = "BANC";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test no window exists', () => {
        /** Test where no window can satisfy the condition. */
        const s = "A";
        const t = "AA";
        const expectedOutput = "";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test empty string', () => {
        /** Test with an empty input string s. */
        const s = "";
        const t = "ABC";
        const expectedOutput = "";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });

    it('test multiple valid windows', () => {
        /** Test with multiple valid windows to ensure the smallest one is returned. */
        const s = "AA";
        const t = "AA";
        const expectedOutput = "AA";
        expect(minWindow(s, t)).toEqual(expectedOutput);
    });
});
