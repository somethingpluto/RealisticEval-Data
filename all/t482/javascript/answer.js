function extractOutermostBrackets(s) {
    /**
     * Extracts the contents of the outermost brackets from the input string.
     *
     * @param {string} s - The input string containing brackets.
     * @returns {string} - The contents within the outermost brackets, or an empty string if no brackets are found.
     */
    let stack = [];
    let startIndex = -1;
    const openingBrackets = "({[";
    const closingBrackets = ")}]";
    const matchingBracket = { ')': '(', '}': '{', ']': '[' };

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (openingBrackets.includes(char)) {  // Check for any opening bracket
            if (stack.length === 0) {  // If the stack is empty, we have found the outermost opening bracket
                startIndex = i;  // Remember the position of the first opening bracket
            }
            stack.push(char);
        } else if (closingBrackets.includes(char)) {  // Check for any closing bracket
            if (stack.length > 0 && stack[stack.length - 1] === matchingBracket[char]) {  // Match with the latest opening bracket
                stack.pop();
                if (stack.length === 0) {  // When stack is empty, we found the outermost closing bracket
                    return s.substring(startIndex + 1, i);  // Extract contents between the brackets
                }
            }
        }
    }

    return "";  // Return an empty string if no outermost brackets were found
}