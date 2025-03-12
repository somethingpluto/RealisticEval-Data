import * as fs from 'fs';
import * as path from 'path';
import * as xregexp from 'xregexp';

interface Mapping {
    regex: RegExp;
    replacement: string;
}

/**
 * Reads question from the given mapping file and returns a list where each element is a tuple containing the compiled regular expression and replacement strings.
 * @param mappingFilePath - Path to the file containing regex mappings.
 * @returns An array of objects, each containing a compiled regex object and a corresponding replacement string.
 */
function readMappingFile(mappingFilePath: string): Mapping[] {
    const fileContent = fs.readFileSync(path.resolve(__dirname, mappingFilePath), 'utf8');
    const lines = fileContent.split(/\r?\n/);
    const mappings: Mapping[] = [];

    lines.forEach(line => {
        const [regexStr, replacementStr] = line.trim().split(/\s+/);
        const regex = xregexp(regexStr);
        mappings.push({ regex, replacement: replacementStr });
    });

    return mappings;
}
interface Mapping {
    regex: RegExp;
    replacement: string;
}
describe('TestReadMappingFile', () => {
    it('test_valid_mapping_file', () => {
        // Test with a valid mapping file content
        const mockFileContent = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n";
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const result = readMappingFile('dummy_path.txt');
        const expected: Mapping[] = [
            { regex: xregexp('old_pattern1'), replacement: 'new_word1' },
            { regex: xregexp('old_pattern2'), replacement: 'new_word2' },
        ];

        expect(result).toEqual(expected);
    });

    it('test_missing_file', () => {
        // Test with a missing file
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => {
            throw new Error('ENOENT: no such file or directory');
        });

        expect(() => readMappingFile('non_existent_file.txt')).toThrow('Unable to find the specified file: non_existent_file.txt');
    });

    it('test_malformed_line_no_comma', () => {
        // Test with a line that does not contain a comma
        const mockFileContent = "'old_pattern1' 'new_word1'\n";
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        expect(() => readMappingFile('dummy_path.txt')).toThrow('Each line must contain exactly one comma separating the pattern and the replacement.');
    });

    it('test_valid_patterns_with_special_characters', () => {
        // Test with valid patterns that contain special regex characters
        const mockFileContent = "'\\d+', 'number'\n'\\w+', 'word'\n";
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const result = readMappingFile('dummy_path.txt');
        const expected: Mapping[] = [
            { regex: xregexp('\\d+'), replacement: 'number' },
            { regex: xregexp('\\w+'), replacement: 'word' },
        ];

        expect(result).toEqual(expected);
    });
});
