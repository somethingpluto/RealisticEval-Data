const fs = require('fs');
const readline = require('readline');

/**
 * Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
 * @param {string} filePath - The path to the file to read.
 * @param {string} word1 - The first word to search for.
 * @param {string} word2 - The second word to search for.
 * @returns {Array} An array containing the line number with the minimum distance and the minimum distance itself.
 *                  Returns [null, Infinity] if one or both words are not found in any line.
 */
function getMinSeqNumAndDistance(filePath, word1, word2) {
    let minDistance = Infinity;
    let minLineNumber = null;

    const fileStream = fs.createReadStream(filePath);
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let lineNumber = 0;

    rl.on('line', (line) => {
        lineNumber++;
        const words = line.split(/\s+/);
        let index1 = -1;
        let index2 = -1;

        for (let i = 0; i < words.length; i++) {
            if (words[i] === word1) {
                index1 = i;
            } else if (words[i] === word2) {
                index2 = i;
            }

            if (index1 !== -1 && index2 !== -1) {
                const distance = Math.abs(index1 - index2);
                if (distance < minDistance) {
                    minDistance = distance;
                    minLineNumber = lineNumber;
                }
            }
        }
    });

    rl.on('close', () => {
        if (minDistance === Infinity) {
            return [null, Infinity];
        } else {
            return [minLineNumber, minDistance];
        }
    });
}
const fs = require('fs');
describe('TestGetMinDistance', () => {
    it('test basic functionality with expected input', () => {
        const mockContent = "hello world\napple banana apple\norange apple banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([2, 1]);
    });

    it('test case where one or both words are not present', () => {
        const mockContent = "apple orange pear\norange pear apple";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test an empty file', () => {
        const mockContent = '';
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([null, Infinity]);
    });

    it('test multiple lines with varying distances between words', () => {
        const mockContent = "apple banana\napple orange orange banana\napple orange orange orange banana";
        const mockFs = {
            readFileSync: jest.fn(() => mockContent),
        };

        global.fs = mockFs;

        const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
        expect([lineNumber, distance]).toEqual([1, 1]);
    });
});
