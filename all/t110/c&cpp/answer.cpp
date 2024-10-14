#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

std::string generateUUID() {
    const std::string possibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const int len = 36;
    std::string uuid;

    // Seed the random number generator
    std::srand(std::time(0));

    for (int i = 0; i < len; ++i) {
        uuid += possibleChars.at(std::rand() % possibleChars.length());
    }

    return uuid;
}
