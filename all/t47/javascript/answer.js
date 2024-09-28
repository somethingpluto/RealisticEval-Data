function findNthWeekdayOfSpecificYear(y, m, n, k) {
    /*
    Calculates the date of the nth occurrence of a specific weekday (k) in a given month (m) and year (y).
    If the nth occurrence does not exist within the month, it returns the last occurrence of that weekday in the month.
    This function extends the capability to handle edge cases where the nth weekday might not be present,
    by providing the closest previous weekday in such cases.
    
    Parameters:
    - y (int): The year for which the date is to be calculated.
    - m (int): The month for which the date is to be calculated, where January is 1 and December is 12.
    - n (int): The nth occurrence of the weekday within the month. For example, 1 for the first occurrence, 2 for the second, etc.
    - k (int): The weekday, where Monday is 0 and Sunday is 6.

    Returns:
    - Date: The calculated date of the nth occurrence of the weekday in the given month and year.
    If the nth occurrence does not exist, returns the date of the last occurrence of that weekday in the month.
    */

    // Adjust month to be 0-based for JavaScript Date (January is 0)
    let firstDayOfMonth = new Date(y, m - 1, 1);
    
    // Calculate the day difference to the first k weekday
    let dayDifference = (k - firstDayOfMonth.getDay() + 7) % 7;
    let firstKWeekdayOfMonth = new Date(y, m - 1, 1 + dayDifference);
    
    // Calculate the nth occurrence
    let nthKWeekdayOfMonth = new Date(y, m - 1, 1 + dayDifference + (n - 1) * 7);
    
    // Calculate the last day of the month
    let nextMonthFirstDay = m === 12 ? new Date(y + 1, 0, 1) : new Date(y, m, 1);
    let lastDayOfMonth = new Date(nextMonthFirstDay - 1);
    
    if (nthKWeekdayOfMonth > lastDayOfMonth) {
        let lastKWeekdayOfMonth = new Date(lastDayOfMonth);
        lastKWeekdayOfMonth.setDate(lastDayOfMonth.getDate() - (lastDayOfMonth.getDay() - k + 7) % 7);
        return lastKWeekdayOfMonth;
    }

    return nthKWeekdayOfMonth;
}

// Example usage:
console.log(findNthWeekdayOfSpecificYear(2023, 10, 2, 1)); // 2nd Monday of October 2023