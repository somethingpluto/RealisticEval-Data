function* wrapContentGenerator(content: string, width: number = 80): Generator<string> {
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
