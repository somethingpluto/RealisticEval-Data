/**
 * @brief Extracts the name and number from a string in the format "name + number".
 *
 * This helper function splits the input string into its name and number components.
 * It assumes that the string is well-formed, with the name part consisting of alphabetic characters
 * and the number part consisting of numeric digits.
 *
 * @param {string} s The input string in the format "name + number".
 * @return {Object} An object containing the name as a string and the number as an integer.
 */
function extractNameAndNumber(s) {
    let pos = s.length - 1;
    while (pos >= 0 && !isNaN(s[pos]) && s[pos] !== ' ') {
        pos--;
    }
    const name = s.substring(0, pos + 1).trim();
    const number = parseInt(s.substring(pos + 1).trim(), 10);
    return { name, number };
}

/**
 * @brief Sorts the string array with the shape of "name + number" in ascending order. 
 * If the numbers are the same, sorts by name in ascending order, and returns the sorted array.
 *
 * @param {Array<string>} arr An array of strings to be sorted.
 * @return {Array<string>} A sorted array of strings according to the rules described above.
 */
function sortNames(arr) {
    return arr.sort((a, b) => {
        const { name: nameA, number: numberA } = extractNameAndNumber(a);
        const { name: nameB, number: numberB } = extractNameAndNumber(b);
        
        if (numberA !== numberB) {
            return numberA - numberB;
        }
        return nameA.localeCompare(nameB);
    });
}
