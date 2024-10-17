function* wrapContentGenerator(content, width = 80) {
    /**
     * Wrap the text content to the specified maximum width and generate these lines line by line.
     *
     * @param {string} content - The content to be wrapped and yielded line by line.
     * @param {number} width - The maximum width of the lines, default is 80 characters.
     *
     * @yields {string} Each line of the content wrapped to the specified width.
     */
    const lines = content.split('\n');

    for (const line of lines) {
        if (line.trim() === '') {  // Check if the line is essentially empty.
            yield '\n';
        } else {
            let currentLine = '';
            for (let i = 0; i < line.length; i++) {
                if (currentLine.length + line[i].length > width) {
                    yield currentLine;
                    currentLine = line[i];
                } else {
                    currentLine += line[i];
                }
            }
            if (currentLine !== '') {
                yield currentLine;
            }
        }
    }
}