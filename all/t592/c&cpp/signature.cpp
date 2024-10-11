#include <cmath>
#include <stdexcept>

/**
 * @brief Performs a mathematical operation on two operands.
 *
 * This function takes two double values and an operator character, and performs
 * the specified arithmetic operation. Supported operations include addition,
 * subtraction, multiplication, division, and exponentiation.
 *
 * @param a The first operand (double).
 * @param b The second operand (double).
 * @param op A character representing the operation to perform:
 *            '+' for addition,
 *            '-' for subtraction,
 *            '*' for multiplication,
 *            '/' for division,
 *            '^' for exponentiation.
 *
 * @return The result of the operation as a double.
 *
 * @throws std::invalid_argument if the operator is not recognized or if
 *         there is an attempt to divide by zero.
 */
double applyOp(double a, double b, char op) {}