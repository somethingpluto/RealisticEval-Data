/** 
 * Calculates the sum of all elements in an array.
 * 
 * @param {number[]} arr - The array of numbers to sum.
 * @returns {number} The sum of all elements of the array.
 */
function sum(arr: number[]): number {
    if (!Array.isArray(arr)) {
        throw new TypeError('Expected an array of numbers');
    }
    
    return arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
}