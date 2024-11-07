import { isEqual } from 'lodash';

function minWindow(s: string, t: string): string {
    /**
     * Find the minimum window substring in `s` that contains all characters of `t`.
     *
     * Parameters:
     * - s: The input string in which to search for the substring.
     * - t: The target string whose characters must be included in the substring.
     *
     * Returns:
     * - The minimum window substring of `s` that contains all characters of `t`.
     *   Returns an empty string if no such substring exists.
     */

    // If the length of s is less than t, return an empty string
    if (s.length < t.length) {
        return '';
    }

    // Count characters in t
    const substringCounter = countChars(t);
    // Counter for the current window
    let counter = countChars('');

    // Initialize pointers and variables for the minimum window
    let l = 0;
    let r = 0;
    let minLength = Infinity;
    let minString = '';

    // Iterate over s using the right pointer
    for (r = 0; r < s.length; r++) {
        const char = s[r];
        // If the character is in the substringCounter, update the current counter
        if (substringCounter[char]) {
            counter[char] = (counter[char] || 0) + 1;
        }

        // Check if the current window contains all characters in t
        while (isEqual(counter, substringCounter)) {
            // Update the minimum window if a smaller one is found
            if (r - l + 1 < minLength) {
                minLength = r - l + 1;
                minString = s.substring(l, r + 1);
            }

            // Move the left pointer to try to shrink the window
            const leftChar = s[l];
            if (substringCounter[leftChar]) {
                counter[leftChar]--;
                if (counter[leftChar] === 0) {
                    delete counter[leftChar];
                }
            }
            l++;
        }
    }

    // Return the minimum window found or an empty string if none exists
    return minString;
}

// Helper function to count characters in a string
function countChars(str: string): Record<string, number> {
    const result: Record<string, number> = {};
    for (const char of str) {
        result[char] = (result[char] || 0) + 1;
    }
    return result;
}