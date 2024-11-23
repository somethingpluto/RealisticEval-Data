function minWindow(s: string, t: string): string {
    if (s.length < t.length) {
        return '';
    }

    const substringCounter = countChars(t);
    let counter: { [key: string]: number } = {}; // To track the characters in the current window
    let l = 0; // Left pointer
    let r = 0; // Right pointer
    let minLength = Infinity;
    let minString = '';

    // Helper function to count the frequency of each character in a string
    function countChars(str: string): { [key: string]: number } {
        const charCount: { [key: string]: number } = {};
        for (let char of str) {
            charCount[char] = (charCount[char] || 0) + 1;
        }
        return charCount;
    }

    // Helper function to check if the current window contains all characters of t
    function checkCounter(current: { [key: string]: number }, target: { [key: string]: number }): boolean {
        for (const char in target) {
            if (!current[char] || current[char] < target[char]) {
                return false;
            }
        }
        return true;
    }

    // Main logic to find the minimum window substring
    for (r = 0; r < s.length; r++) {
        const char = s[r];
        // If the current character is part of the target string `t`
        if (substringCounter[char]) {
            counter[char] = (counter[char] || 0) + 1;
        }

        // Shrink the window from the left as much as possible while still containing all characters from `t`
        while (checkCounter(counter, substringCounter)) {
            if (r - l + 1 < minLength) {
                minLength = r - l + 1;
                minString = s.substring(l, r + 1);
            }
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

    return minString;
}
