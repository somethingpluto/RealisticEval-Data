function findNthWeekdayOfSpecificYear(y, m, n, k) {
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
     * - k (number): The weekday, where Monday is 1 and Sunday is 7.
     *
     * Returns:
     * - Date: The calculated date of the nth occurrence of the weekday in the given month and year.
     *   If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
     */

    const firstDayOfMonth = new Date(y, m - 1, 1);
    const dayDifference = (k - firstDayOfMonth.getDay() + 7) % 7;
    const firstKWeekdayOfMonth = new Date(firstDayOfMonth.getTime());
    firstKWeekdayOfMonth.setDate(firstDayOfMonth.getDate() + dayDifference);
    const nthKWeekdayOfMonth = new Date(firstKWeekdayOfMonth.getTime());
    nthKWeekdayOfMonth.setDate(firstKWeekdayOfMonth.getDate() + (n - 1) * 7);

    // Calculate the last day of the month
    const nextMonthFirstDay = new Date(y, m, 1);
    const lastDayOfMonth = new Date(nextMonthFirstDay.getTime());
    lastDayOfMonth.setDate(lastDayOfMonth.getDate() - 1);

    if (nthKWeekdayOfMonth > lastDayOfMonth) {
        const lastKWeekdayOfMonth = new Date(lastDayOfMonth.getTime());
        lastKWeekdayOfMonth.setDate(lastDayOfMonth.getDate() - ((lastDayOfMonth.getDay() - k + 7) % 7));
        return lastKWeekdayOfMonth;
    }

    return nthKWeekdayOfMonth;
}