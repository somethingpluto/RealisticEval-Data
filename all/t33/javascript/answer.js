const xml2js = require('xml2js');
const parser = new xml2js.Parser();

/**
 * Convert an XML file into a DataFrame-like structure. Each <sequence> tag is treated as a row,
 * and each sub-element within <sequence> is treated as a column.
 *
 * @param {string} xmlFile - Path to the XML file.
 * @returns {Promise<Array<Object>>} A promise that resolves to an array of objects representing the data.
 */
async function xmlToDataFrame(xmlFile) {
    // Read the XML file
    const fs = require('fs').promises;
    const xmlContent = await fs.readFile(xmlFile, 'utf8');

    // Parse the XML content
    return new Promise((resolve, reject) => {
        parser.parseString(xmlContent, (err, result) => {
            if (err) {
                reject(err);
            } else {
                resolve(result);
            }
        });
    }).then((result) => {
        // Extract the sequences
        const sequences = result.root.sequence;

        // Prepare a list to hold all rows
        const rows = [];

        // Iterate over each <sequence> element in the XML file
        sequences.forEach(sequence => {
            const rowData = {};
            // Iterate over each child of the <sequence> element
            Object.keys(sequence).forEach(childTag => {
                // Use the tag as the column name and the text content as the value
                rowData[childTag] = sequence[childTag][0];
            });
            rows.push(rowData);
        });

        // Return the array of objects representing the data
        return rows;
    });
}