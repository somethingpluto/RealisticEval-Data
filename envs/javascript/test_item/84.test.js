/**
 * Finds the smallest window in the source string that contains all characters of the target string.
 *
 * @param {string} source - The source string in which to search for the window.
 * @param {string} target - The target string containing the characters to be matched.
 * @returns {string} The smallest window in the source string that contains all characters of the target string.
 *                   Returns an empty string if no such window exists.
 */
function findMinWindowSubstring(source, target) {
    if (source.length === 0 || target.length === 0) return "";

    const targetMap = {};
    for (let char of target) {
        targetMap[char] = (targetMap[char] || 0) + 1;
    }

    let requiredChars = Object.keys(targetMap).length;
    let left = 0, right = 0;
    let formed = 0;
    const windowCounts = {};
    let ans = [Infinity, null, null]; // [window length, left, right]

    while (right < source.length) {
        let char = source[right];
        windowCounts[char] = (windowCounts[char] || 0) + 1;

        if (targetMap[char] && windowCounts[char] === targetMap[char]) {
            formed++;
        }

        while (left <= right && formed === requiredChars) {
            char = source[left];

            if (right - left + 1 < ans[0]) {
                ans[0] = right - left + 1;
                ans[1] = left;
                ans[2] = right;
            }

            windowCounts[char]--;
            if (targetMap[char] && windowCounts[char] < targetMap[char]) {
                formed--;
            }

            left++;
        }

        right++;
    }

    return ans[0] === Infinity ? "" : source.slice(ans[1], ans[2] + 1);
}
describe('TestFindMinWindowSubstring', () => {
    it('should return an empty string when source is empty', () => {
        expect(findMinWindowSubstring("", "abc")).toBe("");
    });

    it('should return an empty string when target is empty', () => {
        expect(findMinWindowSubstring("abc", "")).toBe("");
    });

    it('should return an empty string when no valid window exists', () => {
        expect(findMinWindowSubstring("abcdef", "xyz")).toBe("");
    });

    it('should return the entire string when it is an exact match', () => {
        expect(findMinWindowSubstring("abcd", "abcd")).toBe("abcd");
    });

    it('should return "BANC" as the smallest window containing all characters of "ABC"', () => {
        expect(findMinWindowSubstring("ADOBECODEBANC", "ABC")).toBe("BANC");
    });
});
