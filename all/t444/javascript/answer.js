function formatComment(string, maxLength = 60) {
    const lines = string.split('\n');
    const formattedLines = [];
    for (const line of lines) {
        const words = line.split(' ');
        let currentLine = '';
        for (const word of words) {
            if (currentLine.length + word.length > maxLength) {
                formattedLines.push(currentLine);
                currentLine = '';
            }
            if (currentLine === '') {
                currentLine = word;
            } else {
                currentLine += ' ' + word;
            }
        }

        formattedLines.push(currentLine);
    }

    // Return the formatted comment
    return formattedLines.map(line => '# ' + line).join('\n');
}