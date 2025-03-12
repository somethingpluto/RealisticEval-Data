import * as fs from 'fs';
import * as readline from 'readline';

// ... (rest of the class definition)

private async processLine(lineNumber: number, lineContent: string, word1: string, word2: string, distances: number[]): Promise<void> {
  const words = lineContent.split(/\s+/);
  let lastWord1Index = -1;
  let lastWord2Index = -1;

  for (let i = 0; i < words.length; i++) {
    if (words[i] === word1) {
      lastWord1Index = i;
    } else if (words[i] === word2) {
      lastWord2Index = i;
    }

    if (lastWord1Index !== -1 && lastWord2Index !== -1) {
      distances.push(lastWord2Index - lastWord1Index - 1);
      lastWord1Index = -1;
      lastWord2Index = -1;
    }
  }
}

// ... (rest of the class definition)
describe('TestGetMinDistance', () => {
    beforeEach(() => {
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => '');
    });

    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('should handle a simple case', () => {
        const mockFileContent = [
            "hello world",
            "hello hello world",
            "world hello"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });

    it('should handle multiple lines', () => {
        const mockFileContent = [
            "hello planet",
            "world hello planet",
            "hello world planet"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([1, 1]);
    });

    it('should handle large distances', () => {
        const mockFileContent = [
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 27]);
    });

    it('should handle adjacent words', () => {
        const mockFileContent = [
            "hello world",
            "hello hello world world",
            "world hello"
        ].join('\n');

        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(getMinDistance('dummy_file.txt', 'hello', 'world')).toEqual([0, 1]);
    });
});
