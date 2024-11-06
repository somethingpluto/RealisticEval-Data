function formatComment(string: string, maxLength: number = 60): string {
    const lines = string.split('\n');
    let formattedLines: string[] = [];
    for (let line of lines) {
        const words = line.split(' ');
        let currentLine = '';
        for (let word of words) {
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