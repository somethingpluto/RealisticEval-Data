/**
 * Converts a floating-point number to its hexadecimal representation.
 *
 * @param {number} value The float value to be converted to hexadecimal.
 * @return {string} A string containing the hexadecimal representation of the
 *         input float.
 *
 * @note The output string will be in lowercase hexadecimal format.
 */
function floatToHex(value) {
    // Convert the float to its hexadecimal representation
    const buffer = new Float32Array(1);
    buffer[0] = value;
    const intRepresentation = new Uint32Array(buffer.buffer)[0];

    // Convert the unsigned integer to a hexadecimal string
    return intRepresentation.toString(16).padStart(8, '0');
}