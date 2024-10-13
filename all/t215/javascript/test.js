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