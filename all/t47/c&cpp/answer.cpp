#include <iostream>
#include <ctime>

std::tm findNthWeekdayOfSpecificYear(int y, int m, int n, int k) {
    std::tm firstDayOfMonth = {0, 0, 0, 1, m - 1, y - 1900}; // initialize the date to the first day of the month
    std::mktime(&firstDayOfMonth); // normalize the time structure

    int dayDifference = (k - firstDayOfMonth.tm_wday + 7) % 7;
    firstDayOfMonth.tm_mday += dayDifference;
    std::mktime(&firstDayOfMonth); // normalize the time structure again

    firstDayOfMonth.tm_mday += (n - 1) * 7;
    std::time_t nthKWeekdayOfMonth = std::mktime(&firstDayOfMonth); // normalize to ensure the date is valid

    // Calculate the last day of the month
    std::tm nextMonthFirstDay;
    if (m == 12) {
        nextMonthFirstDay = {0, 0, 0, 1, 0, y - 1900 + 1}; 
    } else {
        nextMonthFirstDay = {0, 0, 0, 1, m, y - 1900}; 
    }
    std::mktime(&nextMonthFirstDay); // normalize the time structure
    nextMonthFirstDay.tm_mday -= 1; // go back one day to get the last day of the current month
    std::time_t lastDayOfMonth = std::mktime(&nextMonthFirstDay); 

    if (nthKWeekdayOfMonth > lastDayOfMonth) {
        firstDayOfMonth = nextMonthFirstDay; // set to last day of month
        firstDayOfMonth.tm_mday -= (firstDayOfMonth.tm_wday - k + 7) % 7;
        std::mktime(&firstDayOfMonth); // normalize the time structure
    }

    return firstDayOfMonth;
}

int main() {
    int y, m, n, k;
    std::cout << "Enter year: ";
    std::cin >> y;
    std::cout << "Enter month: ";
    std::cin >> m;
    std::cout << "Enter nth occurrence: ";
    std::cin >> n;
    std::cout << "Enter weekday (0: Monday, ..., 6: Sunday): ";
    std::cin >> k;

    std::tm result = findNthWeekdayOfSpecificYear(y, m, n, k);
    std::cout << "The date is: " << result.tm_year + 1900 << "-"
              << result.tm_mon + 1 << "-" << result.tm_mday << std::endl;

    return 0;
}