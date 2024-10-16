function extractStringFromBraces(input: string): string {
    // Find the position of the first opening brace
    const openingBracePos = input.indexOf('{');

    // Check if an opening brace was found
    if (openingBracePos === -1) {
        return "No opening brace found.";
    }

    // Find the position of the first closing brace after the opening brace
    const closingBracePos = input.indexOf('}', openingBracePos);

    // Check if a closing brace was found
    if (closingBracePos === -1) {
        return "No closing brace found.";
    }

    // Extract the string between the braces (including the braces)
    return input.substring(openingBracePos, closingBracePos + 1);
}