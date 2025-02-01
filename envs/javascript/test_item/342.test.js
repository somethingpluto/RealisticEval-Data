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
    const titles = {
        level1: [],
        level2: [],
        level3: []
    };

    const regex = /#{1,3} (.+)/g;
    let match;
    while ((match = regex.exec(markdown)) !== null) {
        const level = match[0].length;
        const title = match[1];
        titles[`level${level}`].push(title);
    }

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
