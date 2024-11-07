import fs from 'fs'
import path from 'path';
/**
 * Reads a JSON Lines file and returns its content as an array of objects.
 *
 * @param {string} filePath The path to the JSON Lines file.
 * @returns {Promise<Array<Object>>} A promise that resolves to an array of JSON objects parsed from the file.
 * @throws {Error} If the specified file does not exist or there is an error parsing a line in the JSON Lines file.
 */
async function readJsonl(filePath) {
  // Check if the file exists
  if (!fs.existsSync(filePath)) {
    throw new Error(`The file '${filePath}' does not exist.`);
  }

  const jsonList = [];
  const fileStream = fs.createReadStream(filePath, { encoding: 'utf8' });
  let data = '';

  fileStream.on('data', (chunk) => {
    data += chunk;
  });

  return new Promise((resolve, reject) => {
    fileStream.on('end', () => {
      const lines = data.split('\n');
      for (let line of lines) {
        try {
          const jsonObj = JSON.parse(line.trim());
          jsonList.push(jsonObj);
        } catch (error) {
          reject(new Error(`Error parsing line: ${line.trim()} - ${error.message}`));
          return;
        }
      }
      resolve(jsonList);
    });

    fileStream.on('error', (error) => {
      reject(error);
    });
  });
}