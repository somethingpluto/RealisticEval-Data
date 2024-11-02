function getAllAlphabets(): string[] {
    const alphabetCount = 26;
    return Array.from({ length: alphabetCount * 2 }, (_, index) => {
        const charCode = index < alphabetCount
            ? 97 + index
            : 65 + index - alphabetCount;
        return String.fromCharCode(charCode);
    });
}