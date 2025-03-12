// ... (previous code for context)
import { exec } from 'child_process';
import { promisify } from 'util';
const execAsync = promisify(exec);

async function extractBibInfo(bibFile: string): Promise<Array<{ title?: string; author?: string; year?: string }>> {
  try {
    const { stdout } = await execAsync(`python3 parse_bibtex.py ${bibFile}`);
    return JSON.parse(stdout);
  } catch (error) {
    console.error('Error parsing BibTeX file:', error);
    return [];
  }
}
// ... (rest of the code)
describe('TestExtractBibInfo', () => {
    it('test valid entry', () => {
        const mockBib = `@article{sample2024,
            author = {John Doe and Jane Smith},
            title = {A Comprehensive Study on AI},
            year = {2024}
        }`;
        const mockOpen = jest.fn().mockImplementation(() => ({
            readFileSync: jest.fn().mockReturnValue(mockBib),
        }));

        const result = extractBibInfo('dummy.bib');
        const expected = [{ title: 'A Comprehensive Study on AI', author: 'John Doe and Jane Smith', year: '2024' }];
        expect(result).toEqual(expected);
    });

    it('test multiple entries', () => {
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
        const mockOpen = jest.fn().mockImplementation(() => ({
            readFileSync: jest.fn().mockReturnValue(mockBib),
        }));

        const result = extractBibInfo('dummy.bib');
        const expected = [
            { title: 'A Comprehensive Study on AI', author: 'John Doe', year: '2024' },
            { title: 'Deep Learning Techniques', author: 'Jane Smith', year: '2023' }
        ];
        expect(result).toEqual(expected);
    });

    it('test missing fields', () => {
        const mockBib = `@article{sample2024,
            author = {John Doe},
            title = {Title Missing Year}
        }`;
        const mockOpen = jest.fn().mockImplementation(() => ({
            readFileSync: jest.fn().mockReturnValue(mockBib),
        }));

        const result = extractBibInfo('dummy.bib');
        const expected = [{ title: 'Title Missing Year', author: 'John Doe', year: undefined }];
        expect(result).toEqual(expected);
    });

    it('test empty file', () => {
        const mockBib = '';
        const mockOpen = jest.fn().mockImplementation(() => ({
            readFileSync: jest.fn().mockReturnValue(mockBib),
        }));

        const result = extractBibInfo('dummy.bib');
        const expected = [];
        expect(result).toEqual(expected);
    });

    it('test incorrect format', () => {
        const mockBib = `@article{sample2024,
            author = John Doe,
            title = {Title Without Braces},
            year = 2024
        }`;
        const mockOpen = jest.fn().mockImplementation(() => ({
            readFileSync: jest.fn().mockReturnValue(mockBib),
        }));

        const result = extractBibInfo('dummy.bib');
        const expected = [{ title: 'Title Without Braces', author: undefined, year: undefined }];
        expect(result).toEqual(expected);
    });
});
