/**
 * Filters out all even numbers from an array.
 *
 * @param {number[]} array - The array of numbers to filter.
 * @returns {number[]} - A new array containing only the odd numbers.
 */
function filterOutEvenNumbers(array: number[]): number[] {
    // Use the filter method to return a new array with only odd numbers
    return array.filter(num => num % 2 !== 0);
}