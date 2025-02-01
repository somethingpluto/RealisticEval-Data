/**
 * Filters website content to include lines containing any of the specified keywords as whole words,
 * along with a specified number of lines before and after for context. This version uses regular expressions
 * to ensure exact, whole word matching and respects case sensitivity.
 *
 * @param {string} content - The full text content of the website.
 * @param {Array<string>} keywords - A list of strings to search for within the content.
 * @param {number} [linesBefore=1] - Number of lines to include before a matching line.
 * @param {number} [linesAfter=1] - Number of lines to include after a matching line.
 * @returns {string} - A string containing the filtered content with additional context.
 */
function filterContentWithContext(content, keywords, linesBefore = 1, linesAfter = 1) {
    const lines = content.split('\n');
    const regex = new RegExp(`\\b(${keywords.join('|')})\\b`, 'g');
    const filteredLines = [];

    for (let i = 0; i < lines.length; i++) {
        if (regex.test(lines[i])) {
            const start = Math.max(0, i - linesBefore);
            const end = Math.min(lines.length, i + linesAfter + 1);
            filteredLines.push(...lines.slice(start, end));
            i = end - 1; // Skip the lines that have already been added
        }
    }

    return filteredLines.join('\n');
}
describe('TestFilterContentWithContext', () => {
    describe('Single Keyword Match', () => {
        it('should correctly filter content for a single keyword with context lines', () => {
            const content = `Line one.
            This line contains a keyword.
            Line three.`;
            const keywords = ['keyword'];
            const expectedOutput = `Line one.
            This line contains a keyword.
            Line three.`;
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput.trim());
        });
    });

    describe('No Keyword Match', () => {
        it('should return an empty string when no keywords match', () => {
            const content = `Line one.
            Line two.
            Line three.`;
            const keywords = ['missing'];
            const expectedOutput = '';
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput);
        });
    });

    describe('Lines Before and After', () => {
        it('should correctly include context lines', () => {
            const content = `Line one.
            This line contains a keyword.
            Line three.
            Line four.
            Line five.`;
            const keywords = ['keyword'];
            const expectedOutput = `Line one.
            This line contains a keyword.
            Line three.`;
            const result = filterContentWithContext(content, keywords, 1, 1);
            expect(result.trim()).toEqual(expectedOutput.trim());
        });
    });
});
