import * as fs from 'fs';
import * as csvParser from 'csv-parser';
import * as createCsvWriter from 'csv-writer';
/**
 * Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
 *
 * @param fileHandler - File handler of the CSV file opened in read-plus mode ('r+').
 * @param reader - CSV reader object for reading existing rows.
 * @param rowCandidate - Array containing the new row to be appended.
 */
function appendOrSkipRow(fileHandler: fs.WriteStream, reader: csvParser.CSVParser, rowCandidate: string[]): void {}