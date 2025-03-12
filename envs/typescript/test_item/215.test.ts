import { readFile } from 'fs/promises';
import { createWriteStream } from 'fs';
import { resolve } from 'path';
import { promisify } from 'util';
import { exec } from 'child_process';

const readFileAsync = promisify(readFile);
const writeFileAsync = promisify(createWriteStream.write);

interface ReplacementDict {
  [key: string]: string;
}

async function replaceWordsInFile(filePath: string, replacementDict: ReplacementDict): Promise<string> {
  try {
    const resolvedPath = resolve(__dirname, filePath);
    const fileContent = await readFileAsync(resolvedPath, 'utf8');
    const modifiedContent = fileContent.replace(/\b(\w+)\b/g, (match, word) => {
      return replacementDict[word] || word;
    });

    const outputPath = `${resolvedPath}.modified`;
    const outputStream = createWriteStream(outputPath);
    await outputStream.write(modifiedContent);
    await outputStream.end();

    // Run Python script for post-processing
    const pythonProcess = exec('python post_process.py ${outputPath}');
    await new Promise((resolve, reject) => {
      pythonProcess.on('close', (code) => {
        if (code === 0) {
          resolve();
        } else {
          reject(new Error('Python post-processing script failed'));
        }
      });
    });

    return `File ${outputPath} has been modified and post-processed.`;
  } catch (error) {
    return `Error: ${error.message}`;
  }
}
import fs from 'fs';

describe('TestReplaceWordsInFile', () => {
  const mockFileData = "hello world";

  beforeEach(() => {
    jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileData);
  });

  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('should replace a single word', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = { "hello": "hi" };
    const expected_output = "hi world";

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('should replace multiple words', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = { "hello": "hi", "world": "earth" };
    const expected_output = "hi earth";

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('should not replace any words when no matching keys are present', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = { "goodbye": "bye" };
    const expected_output = "hello world";

    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });

  it('should handle an empty file', () => {
    const file_path = "dummy_path.txt";
    const replacement_dict = { "hello": "hi" };
    const expected_output = "";

    jest.spyOn(fs, 'readFileSync').mockImplementation(() => "");
    const result = replaceWordsInFile(file_path, replacement_dict);
    expect(result).toBe(expected_output);
  });
});
