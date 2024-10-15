#include <iostream>
#include <iomanip>
#include <ctime>

std::string getTime() {
    // Get the current time
    std::time_t now = std::time(nullptr);
    std::tm *localTime = std::localtime(&now);

    // Format the time as 'hh:mm AM/PM'
    std::ostringstream oss;
    oss << std::put_time(localTime, "%I:%M %p");
    return oss.str();
}

int main() {
    std::string currentTime = getTime();
    std::cout << "Current Time: " << currentTime << std::endl;
    return 0;
}