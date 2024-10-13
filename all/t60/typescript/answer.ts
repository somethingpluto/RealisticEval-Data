import * as fs from 'fs';
import * as path from 'path';
import { parse } from 'csv-parser';
import { reduce } from 'extra-static-methods';

interface DataFrame {
  [key: string]: string[];
}

function findCommonColumns(directory: string): string[] {
  const dataframes: DataFrame[] = [];

  // Iterate through all files in the specified directory
  fs.readdir(directory, (err, files) => {
    if (err) throw err;

    files.forEach((filename) => {
      if (filename.endsWith('.csv')) {
        const filepath = path.join(directory, filename);

        // Load the CSV file into a DataFrame
        const df: DataFrame = {};
        parse()
          .on('data', (row: any) => {
            Object.keys(row).forEach((key) => {
              if (!df[key]) {
                df[key] = [];
              }
              df[key].push(row[key]);
            });
          })
          .on('end', () => {
            dataframes.push(df);
          });

        fs.createReadStream(filepath).pipe(parse());
      }
    });

    // Use set intersection to find common columns across all DataFrames
    if (dataframes.length > 0) {
      let commonColumns = new Set(Object.keys(dataframes[0]));
      dataframes.slice(1).forEach((df) => {
        commonColumns = reduce(
          commonColumns,
          (acc, key) => (df[key] ? acc : acc.delete(key)),
          commonColumns
        );
      });
      return Array.from(commonColumns);
    } else {
      // Return an empty list if no CSV files are found
      return [];
    }
  });

  // Since the function is asynchronous, we need to return an empty array initially
  return [];
}
