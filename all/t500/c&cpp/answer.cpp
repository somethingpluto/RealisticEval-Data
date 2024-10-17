#include <iostream>
#include <string>
#include <optional>
#include <sstream>
#include <stdexcept>

// Function to convert a string representation of a score to its decimal value
std::optional<float> convert_score_to_decimal(const std::string& score_str) {
    try {
        // Check if the score is a fraction
        size_t slash_pos = score_str.find('/');
        if (slash_pos != std::string::npos) {
            std::string numerator = score_str.substr(0, slash_pos);
            std::string denominator = score_str.substr(slash_pos + 1);

            // Convert strings to floats
            float num = std::stof(numerator);
            float den = std::stof(denominator);

            // Calculate the decimal value
            float decimal_value = num / den;
            return decimal_value;
        } else {
            // Otherwise, treat it as a decimal
            float decimal_value = std::stof(score_str);
            return decimal_value;
        }
    } catch (const std::invalid_argument& ia) {
        std::cerr << "Error converting '" << score_str << "' to decimal: " << ia.what() << std::endl;
        return std::nullopt;
    } catch (const std::out_of_range& oor) {
        std::cerr << "Error converting '" << score_str << "' to decimal: " << oor.what() << std::endl;
        return std::nullopt;
    } catch (const std::exception& ex) {
        std::cerr << "Error converting '" << score_str << "' to decimal: " << ex.what() << std::endl;
        return std::nullopt;
    }
}