import * as fs from 'fs';
import { createReadStream, ReadStream } from 'fs';
// @ts-ignore
import { parse, ParseOptions } from 'csv-parse';

interface Row {
  [key: string]: any;
}

async function appendOrSkipRow(filePath: string, rowCandidate: Row): Promise<void> {
  const existingRows: Row[] = [];

  // Open the file and create a read stream
  const fileStream: ReadStream = createReadStream(filePath);

  // Configure csv-parse options
  const parserOptions: ParseOptions = {
    columns: true,
    skip_empty_lines: true,
  };

  // Create a csv-parser instance
  const parser = fileStream.pipe(parse(parserOptions));

  // Listen for data events to collect existing rows
  parser.on('data', (row) => {
    existingRows.push(row);
  });

  // Wait for the parsing to complete
  await new Promise((resolve, reject) => {
    parser.on('end', resolve);
    parser.on('error', reject);
  });

  // Check if the candidate row already exists in the first three columns
  const rowExists = existingRows.some((existingRow) =>
    Object.keys(existingRow).slice(0, 3).every(
      (key) => existingRow[key] === rowCandidate[key]
    )
  );

  // If the row does not exist, append it to the file
  if (!rowExists) {
    const writer = fs.createWriteStream(filePath, { flags: 'a' });
    writer.write(JSON.stringify(rowCandidate) + '\n');
    writer.end();
  }
}