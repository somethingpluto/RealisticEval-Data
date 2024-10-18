#include <iostream>
#include <string>
#include <vector>

// Generates the next sequence in the 'look-and-say' sequence by reading off the digits of the given number,
// grouping by consecutive digits.
std::string look_and_say(const std::string& number) {
    std::vector<std::string> result;
    int count = 1;
    size_t length = number.length();

    // Iterate through the number, group by consecutive digits and count them
    for (size_t i = 1; i < length; ++i) {
        if (number[i] == number[i - 1]) {
            ++count;
        } else {
            result.push_back(std::to_string(count) + std::string(1, number[i - 1]));
            count = 1;
        }
    }

    // Append the last group of digits
    result.push_back(std::to_string(count) + std::string(1, number.back()));

    // Join the result vector into a single string
    std::string finalResult;
    for (const auto& part : result) {
        finalResult += part;
    }

    return finalResult;
}