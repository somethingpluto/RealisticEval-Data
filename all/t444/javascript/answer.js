function formatComment(string, maxLength = 60) {
    /**
     * Formats a string into a commented block with specified maximum line length.
     *
     * @param {string} string - The input string to format.
     * @param {number} maxLength - Maximum length of each line in the output.
     * @returns {string} A formatted string with each line prefixed by '# ' and not exceeding the specified maxLength.
     */
    // Split the string into lines
    const lines = string.split('\n');

    // Initialize an array to store the formatted lines
    const formattedLines = [];

    // Iterate through the lines
    for (const line of lines) {
        // Split the line into words
        const words = line.split(' ');

        // Initialize a variable to keep track of the current line
        let currentLine = '';

        // Iterate through the words
        for (const word of words) {
            // If the current line plus the next word would be too long,
            // append the current line to the list of formatted lines and start a new line
            if (currentLine.length + word.length + 1 > maxLength) {
                formattedLines.push(currentLine);
                currentLine = '';
            }

            // If the current line is empty, add the word to the line
            // Otherwise, add a space and the word to the line
            if (currentLine === '') {
                currentLine = word;
            } else {
                currentLine += ' ' + word;
            }
        }

        // Add the remaining line to the list of formatted lines
        formattedLines.push(currentLine);
    }

    // Return the formatted comment
    return formattedLines.map(line => '# ' + line).join('\n');
}