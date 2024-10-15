#include <iostream>
#include <ctime>

bool isSameDay(std::time_t timestamp1, std::time_t timestamp2) {
    // Convert timestamps to tm struct
    std::tm* date1 = std::localtime(&timestamp1);
    std::tm* date2 = std::localtime(&timestamp2);

    // Compare the year, month, and day of both tm structs
    return (date1->tm_year == date2->tm_year) &&
           (date1->tm_mon == date2->tm_mon) &&
           (date1->tm_mday == date2->tm_mday);
}