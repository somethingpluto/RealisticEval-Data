function convFlags(value: number): string {
    // Create a mask for the first five bits (0x1F = 00011111)
    const mask: number = 0x1F;

    // Invert the first five bits using XOR
    const invertedValue: number = value ^ mask;

    // Convert the result to a hexadecimal string
    return invertedValue.toString(16);
}