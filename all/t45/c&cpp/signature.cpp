/**
 * @brief Returns the current time information including year, month, week of the month, and day of the week.
 *
 * Example output:
 * {
 *     'year': 2024,
 *     'month': 'February',
 *     'week_of_the_month': 5,
 *     'day_of_the_week': 'Thursday'
 * }
 *
 * @param test_date The date to compute information for, defaults to today's date if not provided.
 * @return A map containing the year, month, week of the month, and day of the week.
 */
std::map<std::string, std::string> get_current_date_info(const std::tm* test_date = nullptr) {