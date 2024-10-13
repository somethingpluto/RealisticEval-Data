const fs = require('fs')
const parse5 = require('parse5')

/**
 * Convert an XML file into a 2D array representing a DataFrame. Each <sequence> tag is treated as a row,
 * and each sub-element within <sequence> is treated as a column.
 *
 * Args:
 * xmlFile (string): Path to the XML file.
 *
 * Returns:
 * any[][]: 2D array representing the DataFrame containing the data from the XML file.
 */
function xmlToDataFrame(xmlFile: string): any[][] {
    // Read the XML file
    const xmlContent = fs.readFileSync(xmlFile, 'utf-8');
  
    // Parse the XML content
    const dom = parse5.parse(xmlContent);
    const root = dom.childNodes.find(node => node.nodeName === 'root');
  
    // Prepare a list to hold all rows
    const rows: any[][] = [];
  
    // Iterate over each <sequence> element in the XML file
    root.childNodes.forEach(sequenceNode => {
      if (sequenceNode.nodeName === 'sequence') {
        const rowData: any[] = [];
        sequenceNode.childNodes.forEach(childNode => {
          if (childNode.nodeName !== '#text') {
            // Use the tag as the column name and the text content as the value
            rowData.push(childNode.nodeName);
            rowData.push(childNode.childNodes.find(node => node.nodeName === '#text')?.nodeValue);
          }
        });
        rows.push(rowData);
      }
    });
  
    return rows;
  }