const fs = require('fs').promises;

/**
 * Reads a JSON Lines file and returns its content as an array of objects.
 *
 * @param {string} filePath - The path to the JSON Lines file.
 * @returns {Promise<Array<Object>>} A promise that resolves to an array of JSON objects parsed from the file.
 * @throws {Error} If the specified file does not exist.
 * @throws {SyntaxError} If there is an error parsing a line in the JSON Lines file.
 */
async function readJsonl(filePath) {
    try {
        // Read the file content
        const fileContent = await fs.readFile(filePath, 'utf-8');
        
        // Split the file content by lines
        const lines = fileContent.split('\n');
        
        // Parse each line as a JSON object
        const jsonObjects = lines
            .filter(line => line.trim() !== '') // Remove empty lines
            .map(line => JSON.parse(line)); // Parse each line as JSON
        
        return jsonObjects;
    } catch (error) {
        // Handle file not found or syntax errors
        if (error.code === 'ENOENT') {
            throw new Error(`File not found: ${filePath}`);
        } else if (error instanceof SyntaxError) {
            throw new SyntaxError(`Error parsing JSON in file: ${filePath}`);
        } else {
            throw error;
        }
    }
}
describe('TestReadJsonl', () => {
  let validJsonlFile = 'test_valid.jsonl';
  let invalidJsonlFile = 'test_invalid.jsonl';
  let nonExistentFile = 'non_existent.jsonl';

  beforeAll(() => {
    // Valid JSON Lines content
    fs.writeFileSync(validJsonlFile, '{"name": "Alice", "age": 30}\n' +
      '{"name": "Bob", "age": 25}\n' +
      '{"name": "Charlie", "age": 35}\n');

    // Invalid JSON Lines content
    fs.writeFileSync(invalidJsonlFile, '{"name": "Alice", "age": 30}\n' +
      '{"name": "Bob", "age": "twenty-five}\n');  // Missing closing quote
  });

  afterAll(() => {
    if (fs.existsSync(validJsonlFile)) {
      fs.unlinkSync(validJsonlFile);
    }
    if (fs.existsSync(invalidJsonlFile)) {
      fs.unlinkSync(invalidJsonlFile);
    }
  });

  it('reads a valid JSON Lines file', async () => {
    const expectedData = [
      {"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25},
      {"name": "Charlie", "age": 35}
    ];
    const result = await readJsonl(validJsonlFile);
    expect(result).toEqual(expectedData);
  });

  it('throws an error when the file does not exist', async () => {
    await expect(readJsonl(nonExistentFile)).rejects.toThrow('The file \'non_existent.jsonl\' does not exist.');
  });

  it('reads an empty JSON Lines file', async () => {
    const emptyJsonlFile = 'test_empty.jsonl';
    fs.writeFileSync(emptyJsonlFile, '');  // Create an empty JSON Lines file

    const result = await readJsonl(emptyJsonlFile);
    expect(result).toEqual([]);  // Expecting an empty list for empty file

    fs.unlinkSync(emptyJsonlFile);  // Cleanup after the test
  });
});
