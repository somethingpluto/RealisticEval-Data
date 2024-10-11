#include <iostream>
#include <string>
#include <ctime>

std::string getMonthName(int month) {
    switch(month) {
        case 1: return "January"; break;
        case 2: return "February"; break;
        case 3: return "March"; break;
        case 4: return "April"; break;
        case 5: return "May"; break;
        case 6: return "June"; break;
        case 7: return "July"; break;
        case 8: return "August"; break;
        case 9: return "September"; break;
        case 10: return "October"; break;
        case 11: return "November"; break;
        case 12: return "December"; break;
        default: return ""; break;
    }
}

std::string getDayOfWeekName(int dayOfWeek) {
    switch(dayOfWeek) {
        case 1: return "Monday"; break;
        case 2: return "Tuesday"; break;
        case 3: return "Wednesday"; break;
        case 4: return "Thursday"; break;
        case 5: return "Friday"; break;
        case 6: return "Saturday"; break;
        case 7: return "Sunday"; break;
        default: return ""; break;
    }
}

int getWeekOfMonth(const std::tm &timeInfo) {
    int firstDayOfMonth = std::mktime(new std::tm{timeInfo.tm_year, timeInfo.tm_mon, 1, 0, 0, 0});
    std::tm *firstDayInfo = localtime(&firstDayOfMonth);
    int firstDayWeekday = firstDayInfo->tm_wday + 1; // tm_wday is 0-6, so we add 1 to make it 1-7

    return ((timeInfo.tm_mday - firstDayWeekday + 7) / 7) + 1;
}

std::map<std::string, std::any> getCurrentDateInfo(std::tm *testDate = nullptr) {
    std::map<std::string, std::any> result;

    if (!testDate) {
        time_t now = time(nullptr);
        testDate = localtime(&now);
    }

    result["year"] = testDate->tm_year + 1900;
    result["month"] = getMonthName(testDate->tm_mon + 1);
    result["week_of_the_month"] = getWeekOfMonth(*testDate);
    result["day_of_the_week"] = getDayOfWeekName(testDate->tm_wday + 1);

    return result;
}