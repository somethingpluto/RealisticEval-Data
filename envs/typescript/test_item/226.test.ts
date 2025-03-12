// ... (previous code for context)
import { promisify } from 'util';
import { createReadStream, createWriteStream } from 'fs';
import { parse } from 'csv-parse/lib/sync';
import { stringify } from 'json2csv';
import { Transform } from 'stream';

const readFile = promisify(require('fs').readFile);
const writeFile = promisify(require('fs').writeFile);

function tsvToJsonl(tsvFile: string, jsonlFile: string): Promise<void> {
  return new Promise((resolve, reject) => {
    const readStream = createReadStream(tsvFile);
    const writeStream = createWriteStream(jsonlFile);

    readStream
      .pipe(parse({ delimiter: '\t' }))
      .pipe(new Transform({
        transform(chunk, encoding, callback) {
          const json = stringify(chunk, { rootName: 'record' });
          writeStream.write(`${json}\n`);
          callback();
        },
      }))
      .on('finish', resolve)
      .on('error', reject);
  });
}
// ... (continuation of code)
describe('TSV to JSONL Conversion', () => {
    const tsvFilePath = join(__dirname, '__mocks__', 'example.tsv');
    const jsonlFilePath = join(__dirname, '__mocks__', 'output.jsonl');
  
    beforeAll(() => {
      // Create a mock TSV file for testing
      writeFileSync(tsvFilePath, 'column1\tcolumn2\nvalue1\tvalue2');
    });
  
    afterAll(() => {
      // Clean up the mock files
      try {
        unlinkSync(tsvFilePath);
        unlinkSync(jsonlFilePath);
      } catch (error) {
        console.error(`Error cleaning up mock files: ${error}`);
      }
    });
  
    it('should convert TSV to JSONL successfully', async () => {
      await tsvToJsonl(tsvFilePath, jsonlFilePath);
  
      const expectedJsonlContent = 'column1,column2\nvalue1,value2\n';
      const actualJsonlContent = readFileSync(jsonlFilePath, 'utf-8');
  
      expect(actualJsonlContent).toBe(expectedJsonlContent);
    });
  });
