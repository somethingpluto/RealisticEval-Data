function floatToHex(value: number): string {
    // Convert the float to its hexadecimal representation
    const buffer = new Float32Array(1);
    buffer[0] = value;
    const intRepresentation = new Uint32Array(buffer.buffer)[0];

    // Convert the unsigned integer to a hexadecimal string
    return intRepresentation.toString(16).padStart(8, '0');
}
