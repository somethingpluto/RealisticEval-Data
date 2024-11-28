
import fs from 'fs'
import path from 'path';
import { tmpdir } from 'os';
jest.mock('./formatText', () => ({
    formatText: jest.fn()
}));

describe('TestFormatText', () => {
    afterEach(() => {
        // Clean up after each test
        jest.restoreAllMocks();
    });

    test('test_basic_text', async () => {
        // Test with basic text
        const inputText = "This is line one.\nThis is line two.\nThis is line three.";
        const expectedOutput = "This is line one. This is line two. This is line three.";

        const inputFilePath = path.join(tmpdir(), 'input.txt');
        const outputFilePath = path.join(tmpdir(), 'output.txt');

        // Write input text to a temporary file
        fs.writeFileSync(inputFilePath, inputText);

        // Call the formatText function
        formatText(inputFilePath, outputFilePath);

        // Read the output file
        const outputText = fs.readFileSync(outputFilePath, 'utf8').trim();

        expect(outputText).toEqual(expectedOutput);

        // Clean up
        fs.unlinkSync(inputFilePath);
        fs.unlinkSync(outputFilePath);
    });

    test('test_single_line', async () => {
        // Test with a single line
        const inputText = "This is a single line.";
        const expectedOutput = "This is a single line.";

        const inputFilePath = path.join(tmpdir(), 'input.txt');
        const outputFilePath = path.join(tmpdir(), 'output.txt');

        // Write input text to a temporary file
        fs.writeFileSync(inputFilePath, inputText);

        // Call the formatText function
        formatText(inputFilePath, outputFilePath);

        // Read the output file
        const outputText = fs.readFileSync(outputFilePath, 'utf8').trim();

        expect(outputText).toEqual(expectedOutput);

        // Clean up
        fs.unlinkSync(inputFilePath);
        fs.unlinkSync(outputFilePath);
    });

    test('test_empty_file', async () => {
        // Test with an empty file
        const inputText = "";
        const expectedOutput = "";

        const inputFilePath = path.join(tmpdir(), 'input.txt');
        const outputFilePath = path.join(tmpdir(), 'output.txt');

        // Write input text to a temporary file
        fs.writeFileSync(inputFilePath, inputText);

        // Call the formatText function
        formatText(inputFilePath, outputFilePath);

        // Read the output file
        const outputText = fs.readFileSync(outputFilePath, 'utf8').trim();

        expect(outputText).toEqual(expectedOutput);

        // Clean up
        fs.unlinkSync(inputFilePath);
        fs.unlinkSync(outputFilePath);
    });

    test('test_file_with_no_newlines', async () => {
        // Test with text that has no newlines
        const inputText = "This is a continuous line without breaks.";
        const expectedOutput = "This is a continuous line without breaks.";

        const inputFilePath = path.join(tmpdir(), 'input.txt');
        const outputFilePath = path.join(tmpdir(), 'output.txt');

        // Write input text to a temporary file
        fs.writeFileSync(inputFilePath, inputText);

        // Call the formatText function
        formatText(inputFilePath, outputFilePath);

        // Read the output file
        const outputText = fs.readFileSync(outputFilePath, 'utf8').trim();

        expect(outputText).toEqual(expectedOutput);

        // Clean up
        fs.unlinkSync(inputFilePath);
        fs.unlinkSync(outputFilePath);
    });
});