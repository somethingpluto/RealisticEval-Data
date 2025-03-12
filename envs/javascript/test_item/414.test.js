const fs = require('fs');

/**
 * Extracts the title, author, and year from a BibTeX file.
 * 
 * @param {string} bibFile - The path to the BibTeX file.
 * @returns {Array<Object>} - An array containing objects with title, author, and year for each article.
 */
function extractBibInfo(bibFile) {
    try {
        // Read the content of the BibTeX file
        const content = fs.readFileSync(bibFile, 'utf8');

        // Regular expression to match BibTeX entries
        const bibEntryRegex = /@(\w+)\s*\{\s*([^,]+),\s*([\s\S]*?)\s*\}/g;
        const fieldRegex = /^\s*(\w+)\s*=\s*\{([^}]+)\}/m;

        let match;
        const entries = [];

        // Iterate over each BibTeX entry
        while ((match = bibEntryRegex.exec(content)) !== null) {
            const entryType = match[1];
            const entryKey = match[2];
            const entryContent = match[3];

            const entry = {
                title: null,
                author: null,
                year: null
            };

            // Extract fields from the entry content
            let fieldMatch;
            while ((fieldMatch = fieldRegex.exec(entryContent)) !== null) {
                const fieldName = fieldMatch[1].toLowerCase();
                const fieldValue = fieldMatch[2].trim();

                if (fieldName === 'title') {
                    entry.title = fieldValue;
                } else if (fieldName === 'author') {
                    entry.author = fieldValue;
                } else if (fieldName === 'year') {
                    entry.year = fieldValue;
                }
            }

            // Add the entry to the list if it has the required fields
            if (entry.title && entry.author && entry.year) {
                entries.push(entry);
            }
        }

        return entries;
    } catch (error) {
        console.error('Error reading or parsing BibTeX file:', error);
        return [];
    }
}
const fs = require('fs');
const { mock } = require('jest-mock-extended');


describe('extractBibInfo', () => {
    beforeEach(() => {
        jest.spyOn(fs, 'readFileSync').mockImplementation((path, encoding) => {
            if (path === 'dummy.bib') {
                return 'dummy content';
            }
            return '';
        });
    });

    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('test extraction from a valid BibTeX entry', () => {
        const mockBib = `
            @article{sample2024,
              author = {John Doe and Jane Smith},
              title = {A Comprehensive Study on AI},
              year = {2024}
            }
        `;
        fs.readFileSync.mockReturnValue(mockBib);

        const result = extractBibInfo('dummy.bib');
        const expected = [{
            title: 'A Comprehensive Study on AI',
            author: 'John Doe and Jane Smith',
            year: '2024'
        }];
        expect(result).toEqual(expected);
    });

    it('test extraction from multiple BibTeX entries', () => {
        const mockBib = `
            @article{sample2024,
              author = {John Doe},
              title = {A Comprehensive Study on AI},
              year = {2024}
            }
            @article{sample2023,
              author = {Jane Smith},
              title = {Deep Learning Techniques},
              year = {2023}
            }
        `;
        fs.readFileSync.mockReturnValue(mockBib);

        const result = extractBibInfo('dummy.bib');
        const expected = [
            {
                title: 'A Comprehensive Study on AI',
                author: 'John Doe',
                year: '2024'
            },
            {
                title: 'Deep Learning Techniques',
                author: 'Jane Smith',
                year: '2023'
            }
        ];
        expect(result).toEqual(expected);
    });

    it('test extraction when some fields are missing', () => {
        const mockBib = `
            @article{sample2024,
              author = {John Doe},
              title = {Title Missing Year}
            }
        `;
        fs.readFileSync.mockReturnValue(mockBib);

        const result = extractBibInfo('dummy.bib');
        const expected = [{
            title: 'Title Missing Year',
            author: 'John Doe',
            year: null
        }];
        expect(result).toEqual(expected);
    });

    it('test extraction from an empty BibTeX file', () => {
        const mockBib = '';
        fs.readFileSync.mockReturnValue(mockBib);

        const result = extractBibInfo('dummy.bib');
        const expected = [];
        expect(result).toEqual(expected);
    });

    it('test extraction from a badly formatted BibTeX entry', () => {
        const mockBib = `
            @article{sample2024,
              author = John Doe,
              title = {Title Without Braces},
              year = 2024
            }
        `;
        fs.readFileSync.mockReturnValue(mockBib);

        const result = extractBibInfo('dummy.bib');
        const expected = [{
            title: 'Title Without Braces',
            author: null,
            year: null
        }];
        expect(result).toEqual(expected);
    });
});
