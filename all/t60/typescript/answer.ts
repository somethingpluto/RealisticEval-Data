import fs from 'fs';
import path from 'path';

interface CSVData {
  [key: string]: any;
}

function readCSVFile(filePath: string): CSVData[] {
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const rows = fileContent.split('\n').filter(row => row.trim() !== '');
  const headers = rows[0].split(',').map(header => header.trim());

  return rows.slice(1).map(row => {
    const values = row.split(',').map(value => value.trim());
    const obj: CSVData = {};
    for (let i = 0; i < headers.length; i++) {
      obj[headers[i]] = values[i];
    }
    return obj;
  });
}

function findCommonColumns(directory: string): string[] {
  let allHeaders: Set<string> = new Set();

  fs.readdirSync(directory).forEach(file => {
    if (file.endsWith('.csv')) {
      const filePath = path.join(directory, file);
      const data = readCSVFile(filePath);

      const headers = Object.keys(data[0]);
      headers.forEach(header => allHeaders.add(header));
    }
  });

  // Convert Set to Array
  let commonColumnsArray = Array.from(allHeaders);

  // Filter out columns that appear in only one file
  commonColumnsArray = commonColumnsArray.filter(column => {
    return fs.readdirSync(directory).some(file => {
      if (file.endsWith('.csv')) {
        const filePath = path.join(directory, file);
        const data = readCSVFile(filePath);
        return data.some(row => column in row);
      }
      return false;
    });
  });

  return commonColumnsArray;
}