/**
 * Extracts the title, author, and year from a BibTeX file.
 * Example BibTeX file content:
 * 
 * @article{sample2024,
 *   author = {John Doe and Jane Smith},
 *   title = {A Comprehensive Study on AI},
 *   year = {2024}
 * }
 *
 * @param {string} bibFile - The path to the BibTeX file.
 * @returns {Array<Object>} - An array containing objects with title, author, and year for each article.
 */
function extractBibInfo(bibFile) {
    const fs = require('fs');
    const content = fs.readFileSync(bibFile, 'utf8');
    const regex = /@article\{[^}]*\s*author\s*=\s*{([^}]*)}\s*title\s*=\s*{([^}]*)}\s*year\s*=\s*{([^}]*)}/g;
    const matches = content.matchAll(regex);
    const result = [];

    for (const match of matches) {
        const author = match[1].trim().replace(/ and /g, ', ');
        const title = match[2].trim();
        const year = match[3].trim();
        result.push({ author, title, year });
    }

    return result;
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
