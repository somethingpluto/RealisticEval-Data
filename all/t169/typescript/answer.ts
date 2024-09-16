/**
 * Converts an Arabic numeral to its Roman numeral equivalent.
 *
 * @param {number} num - The number to convert.
 * @returns {string} The Roman numeral representation of the input number.
 * @throws Will throw an error if the input is not a positive integer.
 */
export function convertToRoman(num: number): string {
    if (!Number.isInteger(num) || num <= 0) {
        throw new Error('Input must be a positive integer');
    }

    const romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    const romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    let result = "";

    for (let i = 0; i < romanNumerals.length; i++) {
        while (num >= romanValues[i]) {
            result += romanNumerals[i];
            num -= romanValues[i];
        }
    }

    return result;
}
