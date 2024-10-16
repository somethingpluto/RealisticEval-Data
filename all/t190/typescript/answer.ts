function hexStringToFloat(hexStr: string): number {
    // Convert hex string to integer
    const intValue = parseInt(hexStr, 16);
    
    // Create a Float32Array to convert the integer to a float
    const floatArray = new Float32Array(1);
    const intArray = new Uint32Array(floatArray.buffer);

    // Set the integer value to the Uint32Array
    intArray[0] = intValue;

    // Return the float value
    return floatArray[0];
}