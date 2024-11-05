import * from 'fs'
function tsvToJsonl(tsvFile, jsonlFile) {
  try {
    // Read TSV file content
    const tsvContent = readFileSync(tsvFile, 'utf8');

    // Convert TSV to JSON
    const jsonData = csv({ delimiter: '\t' }).fromString(tsvContent);

    // Convert JSON to JSONL format
    const jsonlContent = jsonData.map(JSON.stringify).join('\n');

    // Write JSONL content to file
    writeFileSync(jsonlFile, jsonlContent, 'utf8');

    console.log(`Successfully converted ${tsvFile} to ${jsonlFile}`);
  } catch (error) {
    console.error('Error converting TSV to JSONL:', error);
  }
}