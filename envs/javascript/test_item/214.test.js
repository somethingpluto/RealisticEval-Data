const fs = require('fs');
const path = require('path');

/**
 * Reads question from the given mapping file and returns an array where each element is a tuple containing the compiled regular expression and replacement strings.
 * 
 * @param {string} mappingFilePath - Path to the file containing regex mappings.
 * @returns {Array} - An array of tuples, where each tuple contains a compiled regex object and a corresponding replacement string.
 * @throws {Error} - Throws an error if the mapping file does not exist or if any line in the file does not contain exactly one comma.
 */
function readMappingFile(mappingFilePath) {
    // Check if the file exists
    if (!fs.existsSync(mappingFilePath)) {
        throw new Error(`File does not exist: ${mappingFilePath}`);
    }

    // Read the file content
    const fileContent = fs.readFileSync(mappingFilePath, 'utf-8');

    // Split the file content by lines
    const lines = fileContent.split('\n').filter(line => line.trim() !== '');

    // Initialize the result array
    const result = [];

    // Process each line
    lines.forEach(line => {
        // Split the line by comma
        const parts = line.split(',');

        // Check if the line contains exactly one comma
        if (parts.length !== 2) {
            throw new Error(`Invalid line in mapping file: ${line}`);
        }

        // Extract the regex pattern and replacement string
        const regexPattern = parts[0].trim();
        const replacementString = parts[1].trim();

        // Compile the regex pattern
        const regex = new RegExp(regexPattern);

        // Add the tuple to the result array
        result.push([regex, replacementString]);
    });

    return result;
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
