function findPlaceholders(text: string): string[] {
    /**
     * Find and return an array of all placeholders in the format {{ placeholder }} from the input text.
     *
     * @param {string} text - The input string containing potential placeholders.
     * @returns {string[]} An array of matching placeholders.
     */
    
    const regex = /\{\{([^}]+)\}\}/g;
    let match: RegExpExecArray | null;
    const placeholders: string[] = [];

    while ((match = regex.exec(text)) !== null) {
        placeholders.push(match[1]);
    }

    return placeholders;
}