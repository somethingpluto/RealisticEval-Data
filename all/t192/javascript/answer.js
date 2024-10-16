function hexStringToUnsignedInt(hexString) {
    // Use parseInt with base 16 to convert hex string to integer
    const result = parseInt(hexString, 16);
    
    // Ensure the result is treated as an unsigned integer
    return result >>> 0; // This ensures it returns a 32-bit unsigned integer
}