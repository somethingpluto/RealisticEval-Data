/**
 * Parses a Markdown table into an array of tuples where each tuple represents a row in the table.
 *
 * @param mdTable - A string representing the Markdown table. The string should include rows separated by newline characters,
 *                  and columns separated by pipes (`|`). The function assumes that the table may include a header separator
 *                  (usually a line of dashes) which will be ignored during parsing.
 *
 * @returns An array of tuples, where each tuple represents a row of the table. The first element of the tuple corresponds to
 *          the first cell in the row (typically the header or first column), and the subsequent elements represent the other
 *          cells in the row. Empty cells will be represented as empty strings.
 *
 * @example
 * const markdownTable = `
 * | Name     | Age | City     |
 * |----------|-----|----------|
 * | Alice    | 25  | New York |
 * | Bob      | 30  | London   |
 * `;
 */
function parseMarkdownTable(mdTable: string): Array<[string, ...string[]]> {}
