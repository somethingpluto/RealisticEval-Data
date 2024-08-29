/**
 * Format the number into a more readable string representation, returning the original form if the number is less than 1,000. If it is greater than or equal to a thousand and less than a million, it is formatted as "x.xK". For a million or more, format it as "x.xM".
 *
 * @param {number} num - The number to be formatted.
 * @returns {string} The formatted number as a string.
 */
export const formatNumber = (num: number): string => {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    } else {
        return num.toString();
    }
};
