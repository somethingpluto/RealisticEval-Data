import * as fs from 'fs';
import * as path from 'path';
import * as csvParser from 'csv-parser';

/**
 * Converts the contents of a CSV file into an SQL insert statement with a table name with the suffix removed.
 * 
 * @param csvFilePath - The path to the CSV file.
 * @returns A string containing the SQL insert statements.
 */
function csvToSqlInsert(csvFilePath: string): string {}