/**
 * Reads tab-separated values (TSV) from standard input and returns a list of rows.
 * 
 * Each row is represented as an array of strings. If rows have unequal lengths,
 * they are padded with empty strings to ensure all rows have the same length.
 * 
 * @returns {Promise<string[][]>} A promise that resolves to a list of lists, where each inner list represents a row of data.
 */
async function readTsvFromStdin(): Promise<string[][]> {}