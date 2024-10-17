#include <iostream>
#include <stdexcept>

class Calculator {
public:
    // Returns the sum of a and b.
    float add(float a, float b) {
        return a + b;
    }

    // Returns the difference of a and b.
    float subtract(float a, float b) {
        return a - b;
    }

    // Returns the product of a and b.
    float multiply(float a, float b) {
        return a * b;
    }

    // Returns the quotient of a and b.
    // Throws std::invalid_argument if b is zero.
    float divide(float a, float b) {
        if (b == 0) {
            throw std::invalid_argument("Cannot divide by zero.");
        }
        return a / b;
    }
};