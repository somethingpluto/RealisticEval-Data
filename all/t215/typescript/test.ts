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