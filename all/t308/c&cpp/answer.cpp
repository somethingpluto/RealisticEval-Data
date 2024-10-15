#include <iostream>
#include <chrono>
#include <iomanip>
#include <sstream>

std::string getCurrentDate() {
    auto now = std::chrono::system_clock::now();
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    std::tm* tm_now = std::localtime(&now_time);

    std::ostringstream oss;
    oss << std::put_time(tm_now, "%Y-%m-%d");
    return oss.str();
}

int main() {
    std::cout << getCurrentDate() << std::endl;
    return 0;
}