struct DateInfo {
    int year;
    std::string month;
    int weekOfMonth;
    std::string dayOfWeek;
};
/*
    Returns the current time information including year, month, week of the month, and day of. eg {
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Thursday'
        }

    Args:
        testDate (std::tm*): The date to compute information for, defaults to today's date if not provided.

    Returns:
        DateInfo: A struct containing the year, month, week of the month, and day of the week.
    */
DateInfo getCurrentDateInfo(std::tm* testDate = nullptr) {}
