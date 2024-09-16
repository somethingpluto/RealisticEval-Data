#include <iostream>

// Function to determine if a year is a leap year
bool is_leap_year(int year) {
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            return year % 400 == 0;
        }
        return true;
    }
    return false;
}

// Function to calculate the number of days in a given month of a given year
int days_in_month(int year, int month) {
    // Array storing the number of days in each month for a non-leap year
    int monthDays[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Check for leap year and adjust February days
    if (month == 2 && is_leap_year(year)) {
        return 29;  // February in a leap year
    }

    return monthDays[month - 1];  // Return the number of days in the month
}