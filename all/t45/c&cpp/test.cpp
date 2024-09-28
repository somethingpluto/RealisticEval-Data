#include <iostream>
#include <ctime>
#include <string>
#include <map>
#include <catch2/catch.hpp>

std::map<std::string, std::string> getCurrentDateInfo(std::tm* test_date = nullptr) {
    std::time_t t = std::time(nullptr);
    std::tm* today;

    if (test_date == nullptr) {
        today = std::localtime(&t);
    } else {
        today = test_date;
    }

    int year = today->tm_year + 1900;
    int month = today->tm_mon + 1;
    int day = today->tm_mday;

    std::string monthNames[] = { "January", "February", "March", "April", "May", "June", "July",
                                 "August", "September", "October", "November", "December" };

    std::string dayNames[] = { "Monday", "Tuesday", "Wednesday", "Thursday", 
                               "Friday", "Saturday", "Sunday" };

    std::string day_of_week = dayNames[today->tm_wday];
    
    // Calculate the week of the month
    std::tm first_day_of_month = *today;
    first_day_of_month.tm_mday = 1;
    std::mktime(&first_day_of_month);

    int first_day_weekday = first_day_of_month.tm_wday;
    int week_of_month = (day + first_day_weekday - 1) / 7 + 1;

    return {
        {"year", std::to_string(year)},
        {"month", monthNames[month - 1]},
        {"week_of_the_month", std::to_string(week_of_month)},
        {"day_of_the_week", day_of_week}
    };
}