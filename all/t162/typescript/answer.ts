/**
 * Converts the array of Boolean values to a binary string representation, which converts to the character 1 if the Boolean value is true. Otherwise, it is converted to the character 0, and the final string is returned
 *
 * @param {boolean[]} boolArray - An array of boolean values.
 * @returns {string} A binary string where '1' represents true and '0' represents false.
 */
function boolArrayToBinaryString(boolArray: boolean[]): string {
    return boolArray.map(bool => (bool ? "1" : "0")).join("");
}
