/**
 * Removes the common leading indentation from each line in a given multi-line string,
 * preserving the relative indentation of the text.
 *
 * @param {string} multilineText - The input string containing multiple lines.
 * @returns {string} The sanitized string with common leading indentation removed.
 */
function removeCommonIndentation(multilineText) {
    const lines = multilineText.split('\n');
    const nonEmptyLines = lines.filter(line => line.trim().length > 0);
    let minIndent = Infinity;
    for (const line of nonEmptyLines) {
        const strippedLine = line.replace(/^\s+/, '');
        const indent = line.length - strippedLine.length;
        minIndent = Math.min(minIndent, indent);
    }
    if (minIndent === Infinity) {
        return multilineText;
    }
    const sanitizedLines = lines.map(line => line.slice(minIndent));
    return sanitizedLines.join('\n');
}