#include <iostream>
#include <ctime>

std::tm calculateGoodFriday(int year) {
    // Anonymous Gregorian algorithm to compute the date of Easter Sunday
    int a = year % 19;
    int b = year / 100;
    int c = year % 100;
    int d = b / 4;
    int e = b % 4;
    int f = (b + 8) / 25;
    int g = (b - f + 1) / 3;
    int h = (19 * a + b - d - g + 15) % 30;
    int i = c / 4;
    int k = c % 4;
    int l = (32 + 2 * e + 2 * i - h - k) % 7;
    int m = (a + 11 * h + 22 * l) / 451;
    int month = (h + l - 7 * m + 114) / 31;
    int day = (h + l - 7 * m + 114) % 31 + 1;

    // Create a tm structure for Easter Sunday
    std::tm easter = {};
    easter.tm_year = year - 1900; // tm_year is year since 1900
    easter.tm_mon = month - 1; // tm_mon is 0-based
    easter.tm_mday = day;

    // Good Friday is two days before Easter Sunday
    std::tm goodFriday = easter;
    goodFriday.tm_mday -= 2; // Subtract 2 days

    // Normalize the tm structure
    std::mktime(&goodFriday);

    return goodFriday;
}
