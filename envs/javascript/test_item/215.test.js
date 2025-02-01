/**
 * Read a text file, replace words according to a dictionary map, and return the modified text.
 *
 * @param {string} file_path - The path to the text file.
 * @param {Object} replacement_dict - An object where the keys are words to be replaced, and the values are the replacement words.
 * @returns {Promise<string>} A promise that resolves to the text with the words replaced or an error message.
 */
async function replaceWordsInFile(file_path, replacement_dict) {
    try {
        // Read the file content
        const fs = require('fs').promises;
        const text = await fs.readFile(file_path, 'utf-8');

        // Replace words according to the dictionary
        let modifiedText = text;
        for (const [key, value] of Object.entries(replacement_dict)) {
            const regex = new RegExp(key, 'gi'); // 'g' for global, 'i' for case-insensitive
            modifiedText = modifiedText.replace(regex, value);
        }

        return modifiedText;
    } catch (error) {
        return `Error reading or processing the file: ${error.message}`;
    }
}
const fs = require('fs');
const { mock } = require('jest-mock-extended');
jest.mock('fs', () => ({
  ...jest.requireActual('fs'),
  readFile: jest.fn(),
}));
describe('replaceWordsInFile', () => {
  beforeEach(() => {
    // Reset the mock implementation before each test
    fs.readFile.mockClear();
  });

  it('replaces a single word', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = {"hello": "hi"};
    const expected_output = "hi world";

    // Mock the file content
    fs.readFile.mockImplementationOnce((path, callback) => {
      callback(null, "hello world");
    });

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('replaces multiple words', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = {"hello": "hi", "world": "earth"};
    const expected_output = "hi earth";

    // Mock the file content
    fs.readFile.mockImplementationOnce((path, callback) => {
      callback(null, "hello world");
    });

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('does not replace non-existent words', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = {"goodbye": "bye"};
    const expected_output = "hello world";

    // Mock the file content
    fs.readFile.mockImplementationOnce((path, callback) => {
      callback(null, "hello world");
    });

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('handles empty files', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = {"hello": "hi"};
    const expected_output = "";

    // Mock the file content
    fs.readFile.mockImplementationOnce((path, callback) => {
      callback(null, "");
    });

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });
});
