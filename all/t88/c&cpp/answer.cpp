#include <iostream>
#include <sstream>
#include <vector>
#include <string>

bool isCronBetween2And4AM(const std::string& cronExpression) {
    std::istringstream stream(cronExpression);
    std::string part;
    std::vector<int> hours;

    // Skip the first part (minute part)
    stream >> part; 
    // Get the hour part
    stream >> part;

    std::istringstream hourStream(part);
    std::string hour;
    while (std::getline(hourStream, hour, ',')) {
        hours.push_back(std::stoi(hour));
    }

    for (int hour : hours) {
        if (hour >= 2 && hour < 4) {
            return true;
        }
    }
    return false;
}