/**
 * @brief Invert the flag bits of an unsigned integer to a hexadecimal string. The number of bits is not complete by 0.
 *
 * @param {number} value The unsigned integer whose bits are to be inverted.
 * @return {string} A string containing the hexadecimal representation of the inverted bits.
 */
function convFlags(value) {
    // Create a mask for the first five bits (0x1F = 00011111)
    const mask = 0x1F;

    // Invert the first five bits using XOR
    const invertedValue = value ^ mask;

    // Convert the result to a hexadecimal string
    return invertedValue.toString(16);
}