/**
 * Format the number into a more readable string representation, returning the original form if the number is less than 1,000. If it is greater than or equal to a thousand and less than a million, it is formatted as "x.xK". For a million or more, format it as "x.xM".
 *
 * @param num - The number to be formatted.
 * @returns The formatted number as a string.
 */
std::string formatNumber(double num);