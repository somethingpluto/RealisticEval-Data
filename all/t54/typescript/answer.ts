/**
 * Processes an array of strings, removing all occurrences of three consecutive backticks from each string.
 *
 * @param {string[]} stringList - The array of strings to process.
 * @returns {string[]} A new array with all instances of three consecutive backticks removed from each string.
 */
function removeTripleBackticks(stringList: string[]): string[] {
    // Use map function to process each string in the array by removing three consecutive backticks
    const processedList = stringList.map(s => s.replace(/```/g, ''));
    return processedList;
}