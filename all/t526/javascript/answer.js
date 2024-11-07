function minWindow(s, t) {
    if (s.length < t.length) {
        return '';
    }
    const substringCounter = countChars(t);
    let counter = {};
    let l = 0;
    let r = 0;
    let minLength = Infinity;
    let minString = '';
    function countChars(str) {
        const charCount = {};
        for (let char of str) {
            charCount[char] = (charCount[char] || 0) + 1;
        }
        return charCount;
    }
    for (r = 0; r < s.length; r++) {
        const char = s[r];
        if (substringCounter[char]) {
            counter[char] = (counter[char] || 0) + 1;
        }
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

function checkCounter(current, target) {
    for (const char in target) {
        if (!current[char] || current[char] < target[char]) {
            return false;
        }
    }
    return true;
}