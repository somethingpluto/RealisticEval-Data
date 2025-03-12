/**
 * Parses markdown text to extract titles of different levels.
 *
 * This function takes a string of markdown content as input and returns an
 * object containing arrays of titles categorized by their level:
 * level 1 (H1), level 2 (H2), and level 3 (H3).
 *
 * @param markdown - A string containing markdown formatted text.
 * @returns An object with three properties: level1, level2, and level3,
 *          each holding an array of corresponding titles found in the markdown.
 */
function parseMarkdownTitles(markdown) {
    // Initialize arrays to hold titles of different levels
    const titles = {
        level1: [],
        level2: [],
        level3: []
    };

    // Split the markdown text into lines
    const lines = markdown.split('\n');

    // Iterate over each line to find and categorize titles
    lines.forEach(line => {
        if (line.startsWith('# ')) {
            titles.level1.push(line.slice(2).trim());
        } else if (line.startsWith('## ')) {
            titles.level2.push(line.slice(3).trim());
        } else if (line.startsWith('### ')) {
            titles.level3.push(line.slice(4).trim());
        }
    });

    return titles;
}
describe('parseMarkdownTitles', () => {
    test('should extract first, second, and third level titles', () => {
        const markdown = `
        # Title 1
        Content here.

        ## Subtitle 1.1
        More content.

        ### Subsubtitle 1.1.1
        Even more content.

        # Title 2
        Another content.
        `;
        const result = parseMarkdownTitles(markdown);
        expect(result).toEqual({
            level1: ["Title 1", "Title 2"],
            level2: ["Subtitle 1.1"],
            level3: ["Subsubtitle 1.1.1"],
        });
    });

    test('should handle missing headers', () => {
        const markdown = `
        This is just some text without headers.
        `;
        const result = parseMarkdownTitles(markdown);
        expect(result).toEqual({
            level1: [],
            level2: [],
            level3: [],
        });
    });

    test('should handle only first-level headers', () => {
        const markdown = `
        # Only Title 1
        Content without subtitles.
        
        # Only Title 2
        More content.
        `;
        const result = parseMarkdownTitles(markdown);
        expect(result).toEqual({
            level1: ["Only Title 1", "Only Title 2"],
            level2: [],
            level3: [],
        });
    });

    test('should handle mixed headers with empty lines', () => {
        const markdown = `
        # Title 1

        ## Subtitle 1.1

        Some content here.

        ### Subsubtitle 1.1.1
        
        # Title 2
        `;
        const result = parseMarkdownTitles(markdown);
        expect(result).toEqual({
            level1: ["Title 1", "Title 2"],
            level2: ["Subtitle 1.1"],
            level3: ["Subsubtitle 1.1.1"],
        });
    });

    test('should handle headers with special characters', () => {
        const markdown = `
        # Title 1 - Special Characters!
        ## Subtitle 1.1: The Beginning
        ### Subsubtitle 1.1.1 (Note)
        `;
        const result = parseMarkdownTitles(markdown);
        expect(result).toEqual({
            level1: ["Title 1 - Special Characters!"],
            level2: ["Subtitle 1.1: The Beginning"],
            level3: ["Subsubtitle 1.1.1 (Note)"],
        });
    });
});
