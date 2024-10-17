function formatStr(x) {
    /**
     * Formats a string by prepending '> ' to each line and ensuring proper
     * formatting of code blocks.
     *
     * @param {any} x - The input to be formatted. If the input is not a
     *                  string, it will be converted to one.
     * @returns {string} - The formatted string with each line prefixed by '> ' and
     *                     with balanced code block delimiters.
     */

    // Convert x to string if it's not already a string.
    if (typeof x !== 'string') {
        x = String(x);
    }

    // Ensure there is a matching number of code block delimiters.
    // If the count of delimiters is odd, append an additional one to balance.
    const delimiterCount = (x.match(/```/g) || []).length;
    if (delimiterCount % 2 === 1) {
        x += "\n```";
    }

    // Format each line by prepending '> ' and join them with newlines.
    const formattedLines = x.split("\n").map(line => "> " + line);

    // Return the final formatted string.
    return formattedLines.join("\n");
}