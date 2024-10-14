#include <iostream>
#include <sstream>
#include <vector>

bool isBreakTime(const std::string& startTime, const std::string& endTime, const std::string& currentTime) {
    auto toMinutes = [](const std::string& time) {
        std::istringstream ss(time);
        std::string hour, minute;
        std::getline(ss, hour, ':');
        std::getline(ss, minute);
        return std::stoi(hour) * 60 + std::stoi(minute);
    };

    int startTotalMinutes = toMinutes(startTime);
    int endTotalMinutes = toMinutes(endTime);
    int currentTotalMinutes = toMinutes(currentTime);

    return currentTotalMinutes >= startTotalMinutes && currentTotalMinutes <= endTotalMinutes;
}