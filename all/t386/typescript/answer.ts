import * as fs from 'fs';
import * as path from 'path';
import * as util from 'util';

const readFileAsync = util.promisify(fs.readFile);
const writeFileAsync = util.promisify(fs.writeFile);

/**
 * This function converts the encoding of a file from one encoding to another.
 *
 * @param inputFilePath - The path to the input file.
 * @param outputFilePath - The path to the output file where the converted content is saved.
 * @param originalEncoding - The original encoding of the file (default is 'cp932').
 * @param targetEncoding - The target encoding to convert to (default is 'utf16').
 * @returns A promise that resolves to true if the conversion was successful, or if no conversion was needed; false otherwise.
 */
async function convertEncoding(
  inputFilePath: string,
  outputFilePath: string,
  originalEncoding: string = 'cp932',
  targetEncoding: string = 'utf16'
): Promise<boolean> {
  try {
    // Read the file with the original encoding
    const content = await readFileAsync(inputFilePath, { encoding: originalEncoding });

    // Write the content in the new encoding
    await writeFileAsync(outputFilePath, content, { encoding: targetEncoding });

    return true;
  } catch (error) {
    if (error instanceof Error && error.name === 'UnicodeDecodeError') {
      try {
        // Check if the file is already in the target encoding
        await readFileAsync(inputFilePath, { encoding: targetEncoding });
        // Copy if no error occurs
        fs.copyFileSync(inputFilePath, outputFilePath);
        console.log(`File already in target encoding: ${inputFilePath}`);
        return true;
      } catch (innerError) {
        if (innerError instanceof Error && innerError.name === 'UnicodeDecodeError') {
          console.error(`Conversion failed due to encoding error: ${error.message}`);
          return false;
        }
      }
    }

    console.error(`Conversion failed due to encoding error: ${error.message}`);
    return false;
  }
}
