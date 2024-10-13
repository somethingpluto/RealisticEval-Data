const {DateTime} = require('luxon')

function findNthWeekdayOfSpecificYear(y: number, m: number, n: number, k: number): DateTime {
    /**
     * Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
     * If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
     * This function extends the capability to handle edge cases where the nth weekday might not be present,
     * by providing the closest previous weekday in such cases.
     *
     * Parameters:
     * - y (number): The year for which the date is to be calculated.
     * - m (number): The month for which the date is to be calculated, where January is 1 and December is 12.
     * - n (number): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
     * - k (number): The weekday, where Monday is 0 and Sunday is 6.
     *
     * Returns:
     * - DateTime: The calculated date of the nth occurrence of the weekday in the given month and year.
     *   If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
     */

    const firstDayOfMonth = DateTime.local(y, m, 1);
    const dayDifference = (k - firstDayOfMonth.weekday + 7) % 7;
    const firstKWeekdayOfMonth = firstDayOfMonth.plus({ days: dayDifference });
    const nthKWeekdayOfMonth = firstKWeekdayOfMonth.plus({ weeks: n - 1 });

    let lastDayOfMonth: DateTime;

    if (m === 12) {
        lastDayOfMonth = DateTime.local(y + 1, 1, 1).minus({ days: 1 });
    } else {
        lastDayOfMonth = DateTime.local(y, m + 1, 1).minus({ days: 1 });
    }

    if (nthKWeekdayOfMonth > lastDayOfMonth) {
        const lastKWeekdayOfMonth = lastDayOfMonth.minus({ days: (lastDayOfMonth.weekday - k + 7) % 7 });
        return lastKWeekdayOfMonth;
    }

    return nthKWeekdayOfMonth;
}