function getAllAlphabets(): string[] {
    const alphabetCount = 26; // Number of letters in the English alphabet
    return Array.from({ length: alphabetCount * 2 }, (_, index) => {
        // Determine the character code based on the index:
        // - If the index is less than 26, it's a lowercase letter ('a' to 'z')
        // - If the index is 26 or greater, it's an uppercase letter ('A' to 'Z')
        const charCode = index < alphabetCount
            ? 97 + index  // Lowercase letters start at char code 97 ('a')
            : 65 + index - alphabetCount; // Uppercase letters start at char code 65 ('A')

        // Convert the character code to a string character
        return String.fromCharCode(charCode);
    });
}