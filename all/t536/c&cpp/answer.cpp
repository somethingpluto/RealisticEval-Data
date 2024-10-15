#include <iostream>
#include <iomanip>
#include <ctime>
#include <locale>

std::string getDate() {
    std::time_t t = std::time(nullptr);
    std::tm* currentTime = std::localtime(&t);

    char buffer[100];
    std::strftime(buffer, sizeof(buffer), "%B %d, %Y", currentTime);
    return std::string(buffer);
}

int main() {
    std::cout << getDate() << std::endl;
    return 0;
}