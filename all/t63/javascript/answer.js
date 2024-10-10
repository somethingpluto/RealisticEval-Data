const fs = require('fs');
const { DataFrame } = require('pandas-js');

function dataframeToMarkdown(df, mdPath) {
    /**
     * Convert a DataFrame object to a table in markdown format.
     * For example:
     *   Input: dataframe {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
     *   Output: | Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n
     *
     * @param {DataFrame} df - DataFrame type object
     * @param {string} mdPath - Output MD file path
     * @returns {string} Markdown file content string
     */

    // Convert DataFrame to markdown
    const headers = df.columns.join(' | ');
    const separator = Array(headers.split(' | ').length).fill('---').join(' | ');
    const rows = df.values.map(row => row.join(' | ')).join('\n');

    const markdownContent = `| ${headers}\n| ${separator}\n| ${rows}`;

    // Write markdown content to file
    fs.writeFileSync(mdPath, markdownContent);

    return markdownContent;
}
