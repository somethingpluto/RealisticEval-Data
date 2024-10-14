#include <iostream>
#include <chrono>
#include <iomanip>
#include <sstream>

std::string timePassed(long long startTimeInMillis) {
    // Get the current time in milliseconds
    auto currentTimeInMillis = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::system_clock::now().time_since_epoch()).count();

    // Calculate the difference in milliseconds
    long long timeDifference = currentTimeInMillis - startTimeInMillis;

    // Convert the difference to seconds
    long long totalSeconds = timeDifference / 1000;

    // Calculate minutes and seconds
    long long minutes = totalSeconds / 60;
    long long seconds = totalSeconds % 60;

    // Format the string
    std::ostringstream oss;
    oss << minutes << ":" << std::setw(2) << std::setfill('0') << seconds;

    return oss.str();
}