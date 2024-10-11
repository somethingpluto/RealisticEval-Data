#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <numeric>

int sum_calibration_values(const std::vector<std::string>& calibration_document) {
    int total_sum = 0;

    for (const auto& line : calibration_document) {
        int first_digit = -1;
        int last_digit = -1;

        for (char ch : line) {
            if (std::isdigit(ch)) {
                if (first_digit == -1) {
                    first_digit = ch - '0';
                }
                last_digit = ch - '0';
            }
        }

        if (first_digit != -1 && last_digit != -1) {
            total_sum += first_digit * 10 + last_digit;
        }
    }

    return total_sum;
}