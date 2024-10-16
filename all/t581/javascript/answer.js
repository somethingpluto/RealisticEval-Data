/**
 * Abbreviates a number to a string with a suffix based on its magnitude.
 *
 * @param {number} number - The number to abbreviate.
 * @returns {string} - The abbreviated string representation of the number.
 */
function abbreviateNumber(number) {
    // If the number is less than 1000, return it as is.
    if (number < 1000) {
        return number.toString();
    }

    // Determine the tier of the number based on its magnitude.
    const tier = Math.floor(Math.log10(number) / 3);

    // Define suffixes for each tier.
    const suffixes = ["", "k", "M", "B", "T"];

    // Calculate the base number by dividing by the corresponding power of ten.
    const baseNumber = number / Math.pow(10, tier * 3);

    // Round the base number to one decimal place.
    const roundedNumber = Math.round(baseNumber * 10) / 10;

    // Return the number with its corresponding suffix.
    return `${roundedNumber}${suffixes[tier]}`;
}