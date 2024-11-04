/**
 * Finds the smallest window in the source string that contains all characters of the target string.
 *
 * @param {string} source - The source string in which to search for the window.
 * @param {string} target - The target string containing the characters to be matched.
 * @returns {string} The smallest window in the source string that contains all characters of the target string.
 *                   Returns an empty string if no such window exists.
 */
function findMinWindowSubstring(source, target) {
    if (!source || !target) {
        return '';
    }
    const requiredChars = countChars(target);
    let windowChars = {};

    let left = 0;  
    let minLength = Infinity;  
    let minWindow = '';  
    function countChars(str) {
        const counter = {};
        for (let char of str) {
            counter[char] = (counter[char] || 0) + 1;
        }
        return counter;
    }
    for (let right = 0; right < source.length; right++) {
        const char = source[right];
        if (requiredChars[char]) {
            windowChars[char] = (windowChars[char] || 0) + 1;
        }
        while (isWindowValid(requiredChars, windowChars)) {
            const windowSize = right - left + 1;
            if (windowSize < minLength) {
                minLength = windowSize;
                minWindow = source.substring(left, right + 1);
            }
            const leftChar = source[left];
            if (requiredChars[leftChar]) {
                windowChars[leftChar]--;
                if (windowChars[leftChar] === 0) {
                    delete windowChars[leftChar];
                }
            }
            left++;
        }
    }

    return minLength <= source.length ? minWindow : '';
}

function isWindowValid(requiredChars, windowChars) {
    for (const char in requiredChars) {
        if ((windowChars[char] || 0) < requiredChars[char]) {
            return false;
        }
    }
    return true;
}