function formatComment(string: string, maxLength: number = 60): string {
    // Split the string into lines
    const lines = string.split('\n');

    // Initialize an array to store the formatted lines
    let formattedLines: string[] = [];

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
            if (currentLine.length + word.length + (currentLine ? 1 : 0) > maxLength) {
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

// Example usage
const exampleString = "This is a very long string that needs to be split into multiple lines with a maximum length of 60 characters.";
console.log(formatComment(exampleString));
