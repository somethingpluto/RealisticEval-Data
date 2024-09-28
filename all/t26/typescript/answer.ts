function convertToCommaSeparated(inputString: string): string {
    /**
     * Converts an input string with multiple separators to a comma-separated string.
     * Now handles additional separators: hyphens (-) and colons (:).
     *
     * @param inputString - The input string containing various separators like *, ;, /, -, :
     * @returns A comma-separated string where all specified separators have been replaced with commas.
     */
    
    // The pattern includes *, ;, /, -, :
    const pattern = /[\*;\/\-\:]/g;  // Correctly escaped hyphen and included colon in the character class
    const commaSeparatedString = inputString.replace(pattern, ',');
    return commaSeparatedString;
}

// Example usage:
const exampleString = "a*b;c/d-e:f";
console.log(convertToCommaSeparated(exampleString));  // Output: "a,b,c,d,e,f"