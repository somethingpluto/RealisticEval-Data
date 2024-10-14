function findMinWindowSubstring(source, target) {
    /**
     * Finds the smallest window in the source string that contains all characters of the target string.
     *
     * @param {string} source - The source string in which to search for the window.
     * @param {string} target - The target string containing the characters to be matched.
     * @returns {string} The smallest window in the source string that contains all characters of the target string.
     *                   Returns an empty string if no such window exists.
     */
    if (!source || !target) {
        return '';
    }

    // Count the frequency of characters in the target string
    const requiredChars = countChars(target);
    // Counter to track characters in the current window of the source string
    let windowChars = {};

    let left = 0;  // Left boundary of the window
    let minLength = Infinity;  // Initialize the minimum length as infinity
    let minWindow = '';  // Initialize the minimum window string

    // Helper function to count characters
    function countChars(str) {
        const counter = {};
        for (let char of str) {
            counter[char] = (counter[char] || 0) + 1;
        }
        return counter;
    }

    // Iterate over the source string with the right boundary of the window
    for (let right = 0; right < source.length; right++) {
        const char = source[right];
        if (requiredChars[char]) {
            windowChars[char] = (windowChars[char] || 0) + 1;
        }

        // Check if the current window contains all characters of the target string
        while (isWindowValid(requiredChars, windowChars)) {
            const windowSize = right - left + 1;
            if (windowSize < minLength) {
                minLength = windowSize;
                minWindow = source.substring(left, right + 1);
            }

            // Attempt to shrink the window from the left
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

// Helper function to check if the current window is valid
function isWindowValid(requiredChars, windowChars) {
    for (const char in requiredChars) {
        if ((windowChars[char] || 0) < requiredChars[char]) {
            return false;
        }
    }
    return true;
}