import { wrap } from 'textwrap';

function* wrapContentGenerator(content: string, width: number = 80): Generator<string> {
    /**
     * Wrap the text content to the specified maximum width and generate these lines line by line.
     *
     * @param content - The content to be wrapped and yielded line by line.
     * @param width - The maximum width of the lines, default is 80 characters.
     *
     * @yields Each line of the content wrapped to the specified width.
     */
    for (const line of content.split(/\r?\n/, width)) {
        if (line.trim() === '') {  // Check if the line is essentially empty.
            yield '\n';
        } else {
            const wrappedLines = wrap(line, { width });
            for (const line2 of wrappedLines) {
                yield line2;
            }
        }
    }
}