/**
 * Reads question from the given mapping file and returns an array where each element is a tuple containing the compiled regular expression and replacement strings.
 * 
 * @param {string} mappingFilePath - Path to the file containing regex mappings.
 * @returns {Array} - An array of tuples, where each tuple contains a compiled regex object and a corresponding replacement string.
 * @throws {Error} - Throws an error if the mapping file does not exist or if any line in the file does not contain exactly one comma.
 */
function readMappingFile(mappingFilePath) {
    const fs = require('fs');
    const path = require('path');

    // Check if the file exists
    if (!fs.existsSync(mappingFilePath)) {
        throw new Error('Mapping file does not exist.');
    }

    // Read the file and split into lines
    const lines = fs.readFileSync(mappingFilePath, 'utf-8').split('\n');

    // Initialize an array to store the tuples
    const tuples = [];

    // Process each line
    for (const line of lines) {
        // Skip empty lines and comments
        if (line.trim() === '' || line.trim().startsWith('//')) {
            continue;
        }

        // Split the line into regex and replacement parts
        const parts = line.split(',');

        // Check if the line contains exactly one comma
        if (parts.length !== 2) {
            throw new Error('Invalid line in mapping file: ' + line);
        }

        // Compile the regex and add it to the array with the replacement string
        try {
            const regex = new RegExp(parts[0].trim(), 'g');
            tuples.push([regex, parts[1].trim()]);
        } catch (error) {
            throw new Error('Invalid regex in mapping file: ' + parts[0]);
        }
    }

    return tuples;
}
jest.mock('fs', () => ({
  ...jest.requireActual('fs'),
  promises: {
    readFile: jest.fn(),
  },
}));

describe('readMappingFile', () => {
  beforeEach(() => {
    jest.resetModules();
    jest.clearAllMocks();
  });

  it('should correctly parse a valid mapping file', () => {
    const mockFileContent = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n";
    const mockPath = '/path/to/dummy_path.txt';
    fs.promises.readFile.mockResolvedValue(mockFileContent);

    return readMappingFile(mockPath).then(result => {
      const expected = [
        [new RegExp('old_pattern1'), 'new_word1'],
        [new RegExp('old_pattern2'), 'new_word2'],
      ];
      expect(result).toEqual(expected);
    });
  });

  it('should throw an error for a missing file', () => {
    const nonExistentFilePath = '/path/to/non_existent_file.txt';
    fs.promises.readFile.mockRejectedValue(new Error('ENOENT'));

    return expect(readMappingFile(nonExistentFilePath)).rejects.toThrow('Unable to find the specified file: /path/to/non_existent_file.txt');
  });

  it('should throw an error for a malformed line without a comma', () => {
    const mockFileContent = "'old_pattern1' 'new_word1'\n";
    const mockPath = '/path/to/dummy_path.txt';
    fs.promises.readFile.mockResolvedValue(mockFileContent);

    return expect(readMappingFile(mockPath)).rejects.toThrow('Each line must contain exactly one comma separating the pattern and the replacement.');
  });

  it('should correctly parse valid patterns with special characters', () => {
    const mockFileContent = "'\\d+', 'number'\n'\\w+', 'word'\n";
    const mockPath = '/path/to/dummy_path.txt';
    fs.promises.readFile.mockResolvedValue(mockFileContent);

    return readMappingFile(mockPath).then(result => {
      const expected = [
        [new RegExp('\\d+'), 'number'],
        [new RegExp('\\w+'), 'word'],
      ];
      expect(result).toEqual(expected);
    });
  });
});
