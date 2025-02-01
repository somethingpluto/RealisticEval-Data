const fs = require('fs');

class WordDistanceFinder {
  /**
   * Find the minimum distance between two specified words (word1 and word2) from the file and return in which line the distance occurred.
   *
   * @param {string} filePath - The path to the file.
   * @param {string} word1 - The first word to search for.
   * @param {string} word2 - The second word to search for.
   * @returns {[number | null, number | null]} - An array containing the line number and the minimum distance, or [null, null] if not found.
   */
  getMinDistance(filePath, word1, word2) {
    let lines = fs.readFileSync(filePath, 'utf-8').split('\n');
    let word1Indexes = [];
    let word2Indexes = [];
    let minDistance = null;
    let lineNumber = null;

    lines.forEach((line, index) => {
      let words = line.trim().split(/\s+/);
      words.forEach((word, wordIndex) => {
        if (word === word1) {
          word1Indexes.push({ line: index + 1, wordIndex });
        } else if (word === word2) {
          word2Indexes.push({ line: index + 1, wordIndex });
        }
      });
    });

    if (word1Indexes.length === 0 || word2Indexes.length === 0) {
      return [null, null];
    }

    word1Indexes.forEach((word1Index) => {
      word2Indexes.forEach((word2Index) => {
        let distance = Math.abs(word1Index.wordIndex - word2Index.wordIndex);
        if (minDistance === null || distance < minDistance) {
          minDistance = distance;
          lineNumber = Math.min(word1Index.line, word2Index.line);
        }
      });
    });

    return [lineNumber, minDistance];
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
