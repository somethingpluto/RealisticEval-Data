function findNthWeekdayOfSpecificYear(year, month, nth, dayOfWeek) {
    const date = new Date(year, month - 1, 1);
    let count = 0;
    while (date.getMonth() === month - 1) {
        if (date.getDay() === dayOfWeek) {
            count++;
            if (count === nth) {
                return date;
            }
        }
        date.setDate(date.getDate() + 1);
    }
    // If nth occurrence does not exist, return the last occurrence of that weekday in the month.
    while (date.getMonth() === month - 1) {
        if (date.getDay() === dayOfWeek) {
            return date;
        }
        date.setDate(date.getDate() - 1);
    }
}