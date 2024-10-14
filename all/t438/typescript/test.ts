import * as Papa from 'papaparse';
import * as fs from 'fs';

/**
 * Reads a CSV file and converts it to a DataFrame-like object.
 *
 * @param filePath - The path to the CSV file.
 * @returns An array of objects representing the data from the CSV file.
 */
export function readCsvToDataframe(filePath: string): Record<string, any>[] | null {
  try {
    if (!fs.existsSync(filePath)) {
      console.error(`Error: The file '${filePath}' was not found.`);
      return null;
    }

    const fileContent = fs.readFileSync(filePath, 'utf8');
    const results = Papa.parse(fileContent, { header: true });

    if (results.errors.length > 0) {
      console.error("Error: Could not parse the file.");
      return null;
    }

    if (results.data.length === 0) {
      console.error("Error: The file is empty.");
      return null;
    }

    return results.data as Record<string, any>[];
  } catch (error) {
    console.error(`An error occurred: ${error}`);
    return null;
  }
}