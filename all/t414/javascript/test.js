import fs from 'fs'
import mock from 'jest-mock-extended'
// Function to extract BibTeX information
function extractBibInfo(bibFile) {
    /**
     * Extracts the title, author, and year from a BibTeX file.
     *
     * @param {string} bibFile - The path to the BibTeX file.
     * @returns {Array<Object>} - An array containing objects with title, author, and year for each article.
     */
    const articles = [];

    // Regular expressions to match title, author, and year
    const titlePattern = /title\s*=\s*{([^}]*)}/i;
    const authorPattern = /author\s*=\s*{([^}]*)}/i;
    const yearPattern = /year\s*=\s*{([^}]*)}/i;

    try {
        const content = fs.readFileSync(bibFile, 'utf8');

        // Split the content into individual entries based on '@'
        const entries = content.split('@').slice(1);  // Skip the first split, which is empty

        for (const entry of entries) {
            const titleMatch = entry.match(titlePattern);
            const authorMatch = entry.match(authorPattern);
            const yearMatch = entry.match(yearPattern);

            // Extracting matched groups if found
            articles.push({
                'title': titleMatch ? titleMatch[1] : null,
                'author': authorMatch ? authorMatch[1] : null,
                'year': yearMatch ? yearMatch[1] : null
            });
        }

    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Error: The file '${bibFile}' was not found.`);
        } else {
            throw error;  // Re-throw the error if it's not a file not found error
        }
    }

    return articles;
}

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