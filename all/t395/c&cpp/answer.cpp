#include <iostream>
#include <vector>
#include <string>
#include <cctype> // For std::isdigit

// Function to sum up calibration values extracted from the document.
// Each calibration value is formed by combining the first and last digits of numbers found in each line
// into a two-digit number.
int sum_calibration_values(const std::vector<std::string>& calibration_document) {
    int total_sum = 0;

    for (const auto& line : calibration_document) {
        std::vector<char> digits;

        // Filter out non-digit characters
        for (char ch : line) {
            if (std::isdigit(ch)) {
                digits.push_back(ch);
            }
        }

        // Extract the first and last digits
        if (!digits.empty()) {
            char first_digit = digits.front();
            char last_digit = digits.back();

            // Combine to form a two-digit number
            int calibration_value = (first_digit - '0') * 10 + (last_digit - '0');

            // Add to the total sum
            total_sum += calibration_value;
        }
    }

    return total_sum;
}