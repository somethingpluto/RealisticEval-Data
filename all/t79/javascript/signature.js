/**
 * Generates a string based on the entered start and end dates. If the start date and end date are in the same month,
 * only one month will be displayed. If not, the start and end months will be displayed separately. For example, if you
 * enter the start date and end date as "2023-08-01" and "2023-08-15" respectively, you will finally output "August 1 to 15, 2023".
 *
 * Example:
 *   Input:
 *     start_date: 2023-08-01
 *     end_date: 2023-08-15
 *   Output:
 *     August 1 to 15, 2023
 *
 * @param {string} start_date - The start date in 'YYYY-MM-DD' format.
 * @param {string} end_date - The end date in 'YYYY-MM-DD' format.
 * @returns {string} A string representing the date range in a human-readable format.
 * @throws {Error} If the start_date or end_date are not in the correct format or if start_date is after end_date.
 */
function dateRangeString(start_date, end_date) {}