import * as fs from 'fs';
import * as readline from 'readline';

interface LineData {
  lineNumber: number;
  lineContent: string;
}

function getMinDistanceBetweenWords(filePath: string, word1: string, word2: string): [number | null, number] {
  let minDistance = Infinity;
  let minLineNumber = null;
  let currentLineNumber = 0;

  const readInterface = readline.createInterface({
    input: fs.createReadStream(filePath),
    output: process.stdout,
    console: false
  });

  readInterface.on('line', (line: string) => {
    currentLineNumber++;
    const words = line.split(/\s+/);
    const index1 = words.indexOf(word1);
    const index2 = words.indexOf(word2);

    if (index1 !== -1 && index2 !== -1) {
      const distance = Math.abs(index1 - index2);
      if (distance < minDistance) {
        minDistance = distance;
        minLineNumber = currentLineNumber;
      }
    }
  });

  return new Promise<[number | null, number]>((resolve) => {
    readInterface.on('close', () => {
      resolve([minLineNumber, minDistance]);
    });
  });
}
import * as fs from 'fs';

describe('TestGetMinDistance', () => {
  it('test basic functionality with expected input', () => {
      const mockContent = "hello world\napple banana apple\norange apple banana";
      const mockOpen = jest.fn().mockImplementation(() => ({
          readFileSync: jest.fn().mockReturnValue(mockContent),
      }));

      // Mock the fs.readFileSync method
      jest.spyOn(fs, 'readFileSync').mockImplementation(mockOpen);

      const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
      expect([lineNumber, distance]).toEqual([2, 1]);

      // Restore the original implementation after the test
      jest.restoreAllMocks();
  });

  it('test case where one or both words are not present', () => {
      const mockContent = "apple orange pear\norange pear apple";
      const mockOpen = jest.fn().mockImplementation(() => ({
          readFileSync: jest.fn().mockReturnValue(mockContent),
      }));

      // Mock the fs.readFileSync method
      jest.spyOn(fs, 'readFileSync').mockImplementation(mockOpen);

      const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
      expect([lineNumber, distance]).toEqual([null, Infinity]);

      // Restore the original implementation after the test
      jest.restoreAllMocks();
  });

  it('test an empty file', () => {
      const mockContent = '';
      const mockOpen = jest.fn().mockImplementation(() => ({
          readFileSync: jest.fn().mockReturnValue(mockContent),
      }));

      // Mock the fs.readFileSync method
      jest.spyOn(fs, 'readFileSync').mockImplementation(mockOpen);

      const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
      expect([lineNumber, distance]).toEqual([null, Infinity]);

      // Restore the original implementation after the test
      jest.restoreAllMocks();
  });

  it('test multiple lines with varying distances between words', () => {
      const mockContent = "apple banana\napple orange orange banana\napple orange orange orange banana";
      const mockOpen = jest.fn().mockImplementation(() => ({
          readFileSync: jest.fn().mockReturnValue(mockContent),
      }));

      // Mock the fs.readFileSync method
      jest.spyOn(fs, 'readFileSync').mockImplementation(mockOpen);

      const [lineNumber, distance] = getMinSeqNumAndDistance('dummy_file.txt', 'apple', 'banana');
      expect([lineNumber, distance]).toEqual([1, 1]);

      // Restore the original implementation after the test
      jest.restoreAllMocks();
  });
});
