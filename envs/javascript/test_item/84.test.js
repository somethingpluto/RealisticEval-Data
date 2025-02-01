/**
 * Finds the smallest window in the source string that contains all characters of the target string.
 *
 * @param {string} source - The source string in which to search for the window.
 * @param {string} target - The target string containing the characters to be matched.
 * @returns {string} The smallest window in the source string that contains all characters of the target string.
 *                   Returns an empty string if no such window exists.
 */
function findMinWindowSubstring(source, target) {
    if (source.length === 0 || target.length === 0 || source.length < target.length) {
        return "";
    }

    let targetMap = {};
    let windowMap = {};
    let required = 0;
    let formed = 0;
    let minLen = Infinity;
    let minStr = "";
    let left = 0;

    // Populate the targetMap and count the required characters
    for (let char of target) {
        targetMap[char] = (targetMap[char] || 0) + 1;
        required++;
    }

    // Iterate through the source string
    for (let right = 0; right < source.length; right++) {
        let char = source[right];
        windowMap[char] = (windowMap[char] || 0) + 1;

        // If the current character is required and its count matches the targetMap, increment formed
        if (targetMap[char] && windowMap[char] === targetMap[char]) {
            formed++;
        }

        // Try and contract the window till the point it ceases to be 'desirable'
        while (left <= right && formed === required) {
            char = source[left];

            // Save the smallest window until now
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStr = source.substring(left, right + 1);
            }

            // The character at the position pointed by the `left` pointer is no longer a part of the window
            windowMap[char]--;
            if (targetMap[char] && windowMap[char] < targetMap[char]) {
                formed--;
            }

            // Move the left pointer ahead, this would help to look for a new window
            left++;
        }
    }

    return minStr;
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
