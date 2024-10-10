#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

bool is_integer(const std::string &str) {
    size_t pos;
    std::stoll(str, &pos);
    return pos == str.length();
}

double is_float(const std::string &str) {
    try {
        size_t pos;
        double val = std::stod(str, &pos);
        if (pos == str.length()) return val;
    } catch (...) {}
    return NAN;
}

struct ConvertResult {
    union {
        int integer;
        double floating_point;
        std::string original_string;
    };
    bool is_original_string;

    ConvertResult(int val) : integer(val), is_original_string(false) {}
    ConvertResult(double val) : floating_point(val), is_original_string(false) {}
    ConvertResult(std::string str) : original_string(str), is_original_string(true) {}

    ~ConvertResult() {
        if (is_original_string) {
            original_string.~basic_string<char>();
        }
    }
};

ConvertResult numerical_str_convert(const std::string &value) {
    if (is_integer(value)) {
        return ConvertResult(std::stoi(value));
    }

    double float_value = is_float(value);
    if (!std::isnan(float_value)) {
        return ConvertResult(float_value);
    }

    return ConvertResult(value);
}
