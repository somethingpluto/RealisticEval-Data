#include <iostream>
#include <cassert>

bool is_compliant_four_digit(int number) {
    /*
     * Determine whether a number is a compliant four-digit number
     *
     * Args:
     *     number (int): The number to check.
     *
     * Returns:
     *     true if the number is a compliant four-digit number, false otherwise.
     */

    // Check if the number is between 1000 and 9999 inclusive
    return (number >= 1000 && number <= 9999);
}