union convertresult {
    int intValue;
    float floatValue;
    std::string stringValue;

    // Destructor to handle cleanup
    ~ConvertResult() {
        // Free memory if stringValue is used
        if (stringValue.data() != nullptr) {
            stringValue.~basic_string();
        }
    }

    // Equality operator to compare union values
    bool operator==(const int& other) const {
        return intValue == other;
    }

    bool operator==(const float& other) const {
        return floatValue == other;
    }

    bool operator==(const std::string& other) const {
        return stringValue == other;
    }
};
/**
 * @brief Convert the input string, first see if it is an integer, if it is converted to an integer,
 * if it is not, see if it is a floating point number, if yes, convert to a floating point number,
 * if neither, return the original string.
 *
 * @param value The input string value.
 * @return A union containing the converted value (int, float, or original string).
 */
ConvertResult numerical_str_convert(const std::string& value) {}