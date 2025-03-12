const fs = require('fs');
const readline = require('readline');

class WordDistanceFinder {
    /**
     * Find the minimum distance between two specified words (word1 and word2) from the file and return in which line the distance occurred.
     *
     * @param {string} filePath - The path to the file.
     * @param {string} word1 - The first word to search for.
     * @param {string} word2 - The second word to search for.
     * @returns {[number | null, number | null]} - An array containing the line number and the minimum distance, or [null, null] if not found.
     */
    static getMinDistance(filePath, word1, word2) {
        return new Promise((resolve, reject) => {
            let minDistance = Infinity;
            let lineNumber = null;
            let lastWord1Index = -1;
            let lastWord2Index = -1;

            const rl = readline.createInterface({
                input: fs.createReadStream(filePath),
                output: process.stdout,
                terminal: false
            });

            rl.on('line', (line) => {
                const words = line.split(/\s+/);
                for (let i = 0; i < words.length; i++) {
                    if (words[i] === word1) {
                        lastWord1Index = i;
                        if (lastWord2Index !== -1) {
                            const distance = Math.abs(lastWord1Index - lastWord2Index);
                            if (distance < minDistance) {
                                minDistance = distance;
                                lineNumber = lineNumber === null ? 1 : lineNumber + 1;
                            }
                        }
                    } else if (words[i] === word2) {
                        lastWord2Index = i;
                        if (lastWord1Index !== -1) {
                            const distance = Math.abs(lastWord1Index - lastWord2Index);
                            if (distance < minDistance) {
                                minDistance = distance;
                                lineNumber = lineNumber === null ? 1 : lineNumber + 1;
                            }
                        }
                    }
                }
            });

            rl.on('close', () => {
                if (minDistance === Infinity) {
                    resolve([null, null]);
                } else {
                    resolve([lineNumber, minDistance]);
                }
            });

            rl.on('error', (err) => {
                reject(err);
            });
        });
    }
}

module.exports = WordDistanceFinder;
const fs = require('fs');

describe('TestGetMinDistance', () => {
    beforeEach(() => {
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => '');
    });

    afterEach(() => {
        fs.readFileSync.mockRestore();
    });

    test('test simple case', () => {
        // Mock the file read operation
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello world
                hello hello world
                world hello
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });

    test('test multiple lines', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello planet
                world hello planet
                hello world planet
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([1, 1]);
    });

    test('test large distance', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello a b c d e f g h i j k l m n o p q r s t u v w x y z world
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 27]);
    });

    test('test adjacent words', () => {
        fs.readFileSync.mockImplementation(() => {
            return Buffer.from(`
                hello world
                hello hello world world
                world hello
            `);
        });

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });
});
