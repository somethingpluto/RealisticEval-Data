/**
 * Calculate the total number of seconds given an array of time periods in the order of
 * days, hours, minutes, and seconds.
 *
 * @param {Array<number>=} time - An array where
 *   time[0] - number of days (optional)
 *   time[1] - number of hours (optional)
 *   time[2] - number of minutes (optional)
 *   time[3] - number of seconds (optional)
 * @returns {number} - The total number of seconds
 *
 * @example
 * calculateTotalSeconds([1, 2, 3, 4]); // returns 93784
 * calculateTotalSeconds([0, 2, 3]); // returns 7380
 */
function calculateTotalSeconds(time = [0, 0, 0, 0]) {}