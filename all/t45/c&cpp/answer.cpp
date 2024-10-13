#include <iostream>
#include <map>
#include <string>
#include <ctime>

// Function to get the English name of the day of the week
std::string getDayName(int dayOfWeek) {
    const std::string daysOfWeek[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    return daysOfWeek[dayOfWeek];
}

// Function to get the English name of the month
std::string getMonthName(int month) {
    const std::string months[] = {"January", "February", "March", "April", "May", "June", 
                                  "July", "August", "September", "October", "November", "December"};
    return months[month - 1]; // Arrays are zero-indexed
}

// Function to calculate the week of the month
int getWeekOfMonth(const std::tm& date) {
    int day = date.tm_mday;
    int firstDayOfWeek = date.tm_wday; // Sunday is 0, Monday is 1, etc.
    return (day + firstDayOfWeek - 1) / 7 + 1;
}

// Function to get current date information
std::map<std::string, std::string> getCurrentDateInfo(const std::tm* test_date = nullptr) {
    std::tm today;
    if (test_date == nullptr) {
        time_t rawTime;
        time(&rawTime);
        today = *localtime(&rawTime);
    } else {
        today = *test_date;
    }

    int year = today.tm_year + 1900;
    int month = today.tm_mon + 1;
    std::string dayOfWeek = getDayName(today.tm_wday);
    std::string monthName = getMonthName(month);
    int weekOfMonth = getWeekOfMonth(today);

    std::map<std::string, std::string> result = {
        {"year", std::to_string(year)},
        {"month", monthName},
        {"week_of_the_month", std::to_string(weekOfMonth)},
        {"day_of_the_week", dayOfWeek}
    };

    return result;
}

int main() {
    // Example usage
    auto currentDateInfo = getCurrentDateInfo();
    for (const auto& info : currentDateInfo) {
        std::cout << info.first << ": " << info.second << std::endl;
    }
    return 0;
}