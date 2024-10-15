#include <iostream>
#include <chrono>
#include <string>
#include <ctime>

struct TimeDifference {
    int days;
    int hours;
    int minutes;
};

TimeDifference calculateTimeDifference(const std::string& givenDate) {
    // Convert the string to time_t
    std::tm tm = {};
    strptime(givenDate.c_str(), "%Y-%m-%d %H:%M:%S", &tm);
    time_t dateToCompare = std::mktime(&tm);
    time_t currentDate = std::time(nullptr);

    // Calculate the difference in seconds
    double differenceInSeconds = std::difftime(currentDate, dateToCompare);

    // If the given date is in the future
    if (differenceInSeconds < 0) {
        return {0, 0, 0};
    }

    // Calculate days, hours, and minutes
    int minutes = static_cast<int>(differenceInSeconds / 60);
    int hours = minutes / 60;
    int days = hours / 24;

    // Calculate remaining hours and minutes
    int remainingHours = hours % 24;
    int remainingMinutes = minutes % 60;

    return {days, remainingHours, remainingMinutes};
}

int main() {
    std::string givenDate = "2024-10-01 12:00:00"; // Example date
    TimeDifference diff = calculateTimeDifference(givenDate);
    std::cout << "Days: " << diff.days << ", Hours: " << diff.hours << ", Minutes: " << diff.minutes << std::endl;
    return 0;
}