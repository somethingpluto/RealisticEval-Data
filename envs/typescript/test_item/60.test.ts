import * as fs from 'fs';
import * as path from 'path';
import * as csv from 'csv-parser';
import { promisify } from 'util';
import { readdir } from 'fs/promises';

const readdirAsync = promisify(readdir);
const readFileAsync = promisify(fs.readFile);

async function findCommonColumns(directory: string): Promise<string[]> {
  const files = await readdirAsync(directory);
  const filePaths = files.map(file => path.join(directory, file));
  const columnCounts = new Map<string, number>();

  for (const filePath of filePaths) {
    if (path.extname(filePath) === '.csv') {
      const columns: string[] = [];
      const stream = fs.createReadStream(filePath).pipe(csv());

      for await (const row of stream) {
        for (const key in row) {
          if (!columns.includes(key)) {
            columns.push(key);
          }
        }
        break; // Assuming CSV files have the same number of columns
      }

      for (const column of columns) {
        const count = columnCounts.get(column) || 0;
        columnCounts.set(column, count + 1);
      }
    }
  }

  return Array.from(columnCounts.entries())
    .filter(([_, count]) => count === filePaths.length)
    .map(([column]) => column);
}
import * as fs from 'fs';
import * as path from 'path';
describe('TestCommonColumns', () => {
  const testDir = 'test_dir';

  beforeEach(() => {
      // Set up a temporary directory
      fs.mkdir(testDir, { recursive: true }, (err) => {
          if (err && err.code !== 'EEXIST') throw err;
      });
  });

  afterEach(() => {
      // Remove created files and directory after each test
      fs.readdir(testDir, (err, files) => {
          if (err) throw err;
          files.forEach(file => {
              fs.unlink(path.join(testDir, file), (unlinkErr) => {
                  if (unlinkErr) throw unlinkErr;
              });
          });
          fs.rmdir(testDir, (rmdirErr) => {
              if (rmdirErr) throw rmdirErr;
          });
      });
  });

  it('should find all same columns', async () => {
      const data1 = "A,B,C\n1,2,3";
      const data2 = "A,B,C\n4,5,6";
      const data3 = "A,B,C\n7,8,9";
      const filenames = ['file1.csv', 'file2.csv', 'file3.csv'];
      const datas = [data1, data2, data3];

      filenames.forEach((filename, index) => {
          fs.writeFile(path.join(testDir, filename), datas[index], (writeErr) => {
              if (writeErr) throw writeErr;
          });
      });

      await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for writes to complete

      const result = findCommonColumns(testDir);
      expect(result).toEqual(['C', 'B', 'A']);
  });

  it('should find no common columns', async () => {
      const data1 = "A,B,C\n1,2,3";
      const data2 = "D,E,F\n4,5,6";
      const data3 = "G,H,I\n7,8,9";
      const filenames = ['file1.csv', 'file2.csv', 'file3.csv'];
      const datas = [data1, data2, data3];

      filenames.forEach((filename, index) => {
          fs.writeFile(path.join(testDir, filename), datas[index], (writeErr) => {
              if (writeErr) throw writeErr;
          });
      });

      await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for writes to complete

      const result = findCommonColumns(testDir);
      expect(result).toEqual([]);
  });

  it('should find some common columns', async () => {
      const data1 = "A,B,C\n1,2,3";
      const data2 = "B,C,D\n4,5,6";
      const data3 = "C,D,E\n7,8,9";
      const filenames = ['file1.csv', 'file2.csv', 'file3.csv'];
      const datas = [data1, data2, data3];

      filenames.forEach((filename, index) => {
          fs.writeFile(path.join(testDir, filename), datas[index], (writeErr) => {
              if (writeErr) throw writeErr;
          });
      });

      await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for writes to complete

      const result = findCommonColumns(testDir);
      expect(result).toEqual(['C']);
  });

  it('should find mixed common and unique columns', async () => {
      const data1 = "A,B,C\n1,2,3";
      const data2 = "B,C,D\n4,5,6";
      const data3 = "B,C,E\n7,8,9";
      const filenames = ['file1.csv', 'file2.csv', 'file3.csv'];
      const datas = [data1, data2, data3];

      filenames.forEach((filename, index) => {
          fs.writeFile(path.join(testDir, filename), datas[index], (writeErr) => {
              if (writeErr) throw writeErr;
          });
      });

      await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for writes to complete

      const result = findCommonColumns(testDir);
      expect(result).toEqual(['B', 'C']);
  });
});
