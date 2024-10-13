const fs = require('fs');
const path = require('path');
const csvParser = require('csv-parser');

/**
 * Converts the contents of a CSV file into an SQL insert statement with a table name with the suffix removed.
 * 
 * @param {string} csvFilePath - The path to the CSV file.
 * @returns {Promise<string>} A promise that resolves to the parsed SQL insert statements.
 */
function csvToSqlInsert(csvFilePath) {}