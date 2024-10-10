/**
 * Reads numerical columns from a file starting from the line after the last line containing '/'.
 *
 * @param file_name - The name of the file to read.
 * @returns A Promise that resolves to a 2D array of numbers.
 * @throws Will throw an error if the file does not contain any '/' character.
 */
async function readColumns(file_name: string): Promise<number[][]> {}