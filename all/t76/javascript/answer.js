function removeCommonIndentation(multilineText) {
    /**
     * Removes the common leading indentation from each line in a given multi-line string,
     * preserving the relative indentation of the text.
     *
     * @param {string} multilineText - The input string containing multiple lines.
     * @returns {string} The sanitized string with common leading indentation removed.
     */
    const lines = multilineText.split('\n');

    // Filter out lines that are empty or only whitespace, as they do not affect minimum indentation
    const nonEmptyLines = lines.filter(line => line.trim().length > 0);

    // Determine the minimum indentation of non-empty lines
    let minIndent = Infinity;
    for (const line of nonEmptyLines) {
        const strippedLine = line.replace(/^\s+/, '');
        const indent = line.length - strippedLine.length;
        minIndent = Math.min(minIndent, indent);
    }

    // If there's no indentation or all lines are empty, return the original string
    if (minIndent === Infinity) {
        return multilineText;
    }

    // Remove the common leading indentation from each line
    const sanitizedLines = lines.map(line => line.slice(minIndent));

    return sanitizedLines.join('\n');
}