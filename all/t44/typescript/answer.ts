function alignLinesLeft(str1: string, str2: string): [string, string] {
    /**
     * Align two lines of string to the left, supplementing with Spaces if the length is not enough
     *
     * @param {string} str1 - The first string
     * @param {string} str2 - The second string
     * @returns {[string, string]} - Aligned str1 and str2
     */
    
    // Determine the maximum length between the two strings
    const maxLength = Math.max(str1.length, str2.length);
    
    // Pad both strings with spaces to match the maximum length
    const paddedStr1 = str1.padEnd(maxLength);
    const paddedStr2 = str2.padEnd(maxLength);
    
    return [paddedStr1, paddedStr2];
}