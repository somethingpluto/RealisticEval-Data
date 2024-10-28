import * as fs from 'fs';

/**
 * Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
 * @param filePath The path to the file to read.
 * @param word1 The first word to search for.
 * @param word2 The second word to search for.
 * @returns A tuple containing the line number with the minimum distance and the minimum distance itself.
 *          Returns [null, Infinity] if one or both words are not found in any line.
 */
function getMinSeqNumAndDistance(filePath: string, word1: string, word2: string): [number | null, number] {}