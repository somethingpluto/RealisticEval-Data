function splitString(str: string): string[] {
    const result: string[] = [];
    const words = str.split(/\s+/); // Split by whitespace

    for (const word of words) {
        if (word) { // Avoid pushing empty strings
            result.push(word);
        }
    }

    return result;
}