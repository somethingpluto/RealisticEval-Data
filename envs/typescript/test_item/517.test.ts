import * as fs from 'fs';
import * as path from 'path';

/**
 * Reads a JSON Lines file and returns its content as an array of objects.
 * ...
 */

function readJsonl(file_path: string): Array<{ [key: string]: any }> {
  if (!fs.existsSync(file_path)) {
    throw new Error(`File does not exist: ${file_path}`);
  }

  const content = fs.readFileSync(file_path, 'utf8');
  const lines = content.split('\n');
  const jsonArray = [];

  for (const line of lines) {
    if (line.trim() === '') continue; // Skip empty lines
    try {
      jsonArray.push(JSON.parse(line));
    } catch (error) {
      throw new SyntaxError(`Error parsing line: ${line}`);
    }
  }

  return jsonArray;
}
describe('TestReadJsonl', () => {
   let validJsonlFile: string;
   let invalidJsonlFile: string;
   let nonExistentFile: string;
   let emptyJsonlFile: string;

   beforeAll(() => {
       // Create temporary JSON Lines files for testing
       validJsonlFile = 'test_valid.jsonl';
       invalidJsonlFile = 'test_invalid.jsonl';
       nonExistentFile = 'non_existent.jsonl';
       emptyJsonlFile = 'test_empty.jsonl';

       // Valid JSON Lines content
       fs.writeFileSync(validJsonlFile, '{"name": "Alice", "age": 30}\n' +
                           '{"name": "Bob", "age": 25}\n' +
                           '{"name": "Charlie", "age": 35}\n');

       // Invalid JSON Lines content
       fs.writeFileSync(invalidJsonlFile, '{"name": "Alice", "age": 30}\n' +
                             '{"name": "Bob", "age": "twenty-five}\n');  // Missing closing quote
   });

   afterAll(() => {
       // Remove the temporary JSON Lines files after testing
       if (fs.existsSync(validJsonlFile)) {
           fs.unlinkSync(validJsonlFile);
       }
       if (fs.existsSync(invalidJsonlFile)) {
           fs.unlinkSync(invalidJsonlFile);
       }
       if (fs.existsSync(emptyJsonlFile)) {
           fs.unlinkSync(emptyJsonlFile);
       }
   });

   it('should read a valid JSON Lines file correctly', () => {
       const expectedData = [
           {"name": "Alice", "age": 30},
           {"name": "Bob", "age": 25},
           {"name": "Charlie", "age": 35}
       ];
       const result = readJsonl(validJsonlFile);
       expect(result).toEqual(expectedData);
   });

   it('should throw an error when the file does not exist', () => {
       expect(() => readJsonl(nonExistentFile)).toThrow(Error);
   });

   it('should handle an empty JSON Lines file correctly', () => {
       fs.writeFileSync(emptyJsonlFile, '');  // Create an empty JSON Lines file
       const result = readJsonl(emptyJsonlFile);
       expect(result).toEqual([]);  // Expecting an empty list for empty file
   });
});
