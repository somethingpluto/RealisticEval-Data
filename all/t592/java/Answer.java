package org.real.temp;

/**
 * Performs a mathematical operation on two operands.
 * <p>
 * This function takes two double values and an operator character, and performs
 * the specified arithmetic operation. Supported operations include addition,
 * subtraction, multiplication, division, and exponentiation.
 * </p>
 *
 * @param a The first operand (double).
 * @param b The second operand (double).
 * @param op A character representing the operation to perform:
 *           '+' for addition,
 *           '-' for subtraction,
 *           '*' for multiplication,
 *           '/' for division,
 *           '^' for exponentiation.
 * @return The result of the operation as a double.
 * @throws IllegalArgumentException if the operator is not recognized or if
 *                                  there is an attempt to divide by zero.
 */
public class Answer {
    public static double applyOp(double a, double b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/':
                if (b == 0) {
                    throw new IllegalArgumentException("Division by zero is not allowed.");
                }
                return a / b;
            case '^': return Math.pow(a, b);
            default:
                throw new IllegalArgumentException("Invalid operator.");
        }
    }
}