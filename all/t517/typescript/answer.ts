import fs from 'fs';
import { JSONParseError } from 'json5';

/**
* Reads a JSON Lines file and returns its content as an array of objects.
*
* @param file_path - The path to the JSON Lines file.
* @returns An array of JSON objects parsed from the file.
* @throws {Error} If the specified file does not exist or there is an error parsing a line in the JSON Lines file.
*/
function readJsonl(file_path: string): Array<{ [key: string]: any }> {
   // Check if the file exists
   if (!fs.existsSync(file_path)) {
       throw new Error(`The file '${file_path}' does not exist.`);
   }

   const jsonList: Array<{ [key: string]: any }> = [];
   const fileContent = fs.readFileSync(file_path, 'utf8');
   const lines = fileContent.split('\n');

   for (const line of lines) {
       try {
           const jsonObj = JSON.parse(line);
           jsonList.push(jsonObj);
       } catch (error) {
           if (error instanceof JSONParseError) {
               throw new Error(`Error parsing line: ${line.trim()} - ${error.message}`);
           }
       }
   }

   return jsonList;
}

// Example usage
try {
   const filePath = './example.jsonl';
   const data = readJsonl(filePath);
   console.log(data);
} catch (error) {
   console.error(error);
}