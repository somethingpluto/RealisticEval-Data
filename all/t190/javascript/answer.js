function hexStringToFloat(hexStr) {
    // Convert hexadecimal string to an integer
    const intValue = parseInt(hexStr, 16);
    
    // Create a Float32Array to interpret the bits as a float
    const floatArray = new Float32Array(1);
    const uintArray = new Uint32Array(floatArray.buffer);

    // Assign the integer value to the Uint32Array
    uintArray[0] = intValue;

    // Return the float value
    return floatArray[0];
}