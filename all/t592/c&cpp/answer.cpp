#include <cmath>
#include <stdexcept>

double applyOp(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0) {
                throw std::invalid_argument("Division by zero is not allowed.");
            }
            return a / b;
        case '^': return pow(a, b);
        default:
            throw std::invalid_argument("Invalid operator.");
    }
}