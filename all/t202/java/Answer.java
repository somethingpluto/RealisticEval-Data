package org.real.temp;

public class Answer {
    /**
     * @brief Returns the number of days in a given month of a specific year.
     *
     * This function accounts for leap years when calculating the number of days in February.
     *
     * @param year The year for which to get the number of days in the month. This should be
     *             a valid integer representing a year (e.g., 2024).
     * @param month The month for which to get the number of days. It should be an integer
     *              between 1 and 12, where 1 corresponds to January and 12 to December.
     * @return The number of days in the specified month of the specified year.
     *
     * @throws IllegalArgumentException if the month is not between 1 and 12.
     */
    public static int getDaysInMonth(int year, int month) {
        // Check if the month is valid
        if (month < 1 || month > 12) {
            throw new IllegalArgumentException("Month must be between 1 and 12.");
        }

        // Array of days in each month, index 0 is unused, 1-12 represent Jan-Dec
        final int[] daysInMonth = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Handle February's case
        if (month == 2) {
            // Check if it's a leap year
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                return 29; // Leap year
            } else {
                return 28; // Non-leap year
            }
        }

        // Return the number of days for the specified month
        return daysInMonth[month];
    }
}