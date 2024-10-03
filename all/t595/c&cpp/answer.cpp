#include <iostream>
#include <stdexcept> // for std::invalid_argument

using namespace std;



/**
 * @brief Returns the number of days in a given month of a given year.
 *
 * This function accounts for leap years when determining the number of
 * days in February. It throws an exception if the month is invalid.
 *
 * @param year The year to check (should be a positive integer).
 * @param month The month to check (1 for January, 12 for December).
 * @return int The number of days in the specified month of the specified year.
 * @throws std::invalid_argument If the month is not between 1 and 12.
 */
int getDaysInMonth(int year, int month) {
    // Array storing the number of days in each month (index 0 is unused)
    const int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    // Validate month input
    if (month < 1 || month > 12) {
        throw std::invalid_argument("Month must be between 1 and 12");
    }

    // Adjust for leap years if the month is February (month == 2)
    if (month == 2) {
        bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        return isLeapYear ? 29 : 28; // Return 29 if leap year, otherwise 28
    }

    // Return the number of days in the specified month
    return daysInMonth[month];
}