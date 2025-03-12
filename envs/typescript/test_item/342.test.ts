// ... (previous code for context)
import { execSync } from 'child_process';

function parseMarkdownTitles(markdown: string): { level1: string[]; level2: string[]; level3: string[] } {
  const { level1, level2, level3 } = parseMarkdown(markdown);
  const pythonScriptPath = './process_titles.py';

  try {
    const level1Processed = execSync(`python ${pythonScriptPath} '${level1.join("', '")}'`).toString().trim();
    const level2Processed = execSync(`python ${pythonScriptPath} '${level2.join("', '")}'`).toString().trim();
    const level3Processed = execSync(`python ${pythonScriptPath} '${level3.join("', '")}'`).toString().trim();

    return {
      level1: level1Processed.split("'"),
      level2: level2Processed.split("'"),
      level3: level3Processed.split("'"),
    };
  } catch (error) {
    console.error('Error calling Python script:', error);
    throw error;
  }
}
// ... (rest of the code)
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
