import fs from 'fs';
import { difference } from 'lodash';

interface FileCompareResult {
  differences: string[];
}

export function compareFiles(file1Path: string, file2Path: string): Promise<FileCompareResult> {
  return new Promise((resolve, reject) => {
    fs.readFile(file1Path, 'utf8', (err, data1) => {
      if (err) {
        return reject(err);
      }

      fs.readFile(file2Path, 'utf8', (err, data2) => {
        if (err) {
          return reject(err);
        }

        const differences = difference(data1.split('\n'), data2.split('\n'));
        
        resolve({differences});
      });
    });
  });
}