#include <iostream>
#include <string>
#include <iomanip> // for std::setw and std::setfill

std::string formatThreadCount(int count) {
    // Handle the case when there are no threads
    if (count == 0) {
        return "No Threads";
    }

    // Format the count to ensure at least 2 digits
    std::string threadCount = (count < 10 ? "0" : "") + std::to_string(count);

    // Determine the correct word form based on the count
    std::string threadWord = (count == 1) ? "Thread" : "Threads";

    // Return the formatted string
    return threadCount + " " + threadWord;
}