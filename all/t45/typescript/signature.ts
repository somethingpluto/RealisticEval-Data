/**
 * Returns the current time information including year, month, week of the month, and day of the week.
 * Example output:
 * {
 *     'year': 2024,
 *     'month': 'February',
 *     'week_of_the_month': 5,
 *     'day_of_the_week': 'Thursday'
 * }
 *
 * @param testDate - The date to compute information for, defaults to today's date if not provided.
 * @returns A dictionary containing the year, month, week of the month, and day of the week.
 */
function getCurrentDateInfo(testDate?: DateTime): { year: number; month: string; weekOfTheMonth: number; dayOfWeek: string } {}