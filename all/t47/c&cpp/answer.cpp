#include <iostream>
#include <ctime>

// Function to calculate the date of the nth occurrence of a specific weekday in a given month and year
std::tm findNthWeekdayOfSpecificYear(int y, int m, int n, int k) {
    // Initialize time structure
    std::tm t = {0};
    t.tm_year = y - 1900; // tm_year is years since 1900
    t.tm_mon = m - 1;     // tm_mon is months since January

    // Find the first day of the specified month
    mktime(&t);
    
    // Calculate the number of days to reach the nth weekday
    int dayOfWeek = t.tm_wday;
    if ((n * 7 + dayOfWeek) >= 31) {
        n--;
    }
    int daysToAdd = n * 7 + k - dayOfWeek;

    // Add the calculated days to get the desired date
    t.tm_mday += daysToAdd;
    mktime(&t);

    return t;
}