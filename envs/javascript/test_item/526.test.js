/**
 * Find the minimum window substring in `s` that contains all characters of `t`.
 *
 * @param {string} s - The input string in which to search for the substring.
 * @param {string} t - The target string whose characters must be included in the substring.
 * @returns {string} The minimum window substring of `s` that contains all characters of `t`.
 *                   Returns an empty string if no such substring exists.
 */
function minWindow(s, t) {
    if (s.length === 0 || t.length === 0) return "";

    const need = {};
    const window = {};

    for (let char of t) {
        need[char] = (need[char] || 0) + 1;
    }

    let left = 0, right = 0;
    let valid = 0;
    let start = 0, length = Infinity;

    while (right < s.length) {
        const c = s[right];
        right++;
        if (need[c]) {
            window[c] = (window[c] || 0) + 1;
            if (window[c] === need[c]) {
                valid++;
            }
        }

        while (valid === Object.keys(need).length) {
            if (right - left < length) {
                start = left;
                length = right - left;
            }
            const d = s[left];
            left++;
            if (need[d]) {
                if (window[d] === need[d]) {
                    valid--;
                }
                window[d]--;
            }
        }
    }

    return length === Infinity ? "" : s.substring(start, start + length);
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
