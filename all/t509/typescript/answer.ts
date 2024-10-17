function modExp(base: number, exponent: number, modulus: number): number {
    if (modulus <= 0) {
        throw new Error("Modulus must be a positive integer.");
    }

    let result = 1;
    base = base % modulus;  // Ensure base is within the modulus

    while (exponent > 0) {
        // If exponent is odd, multiply the base with the result
        if (exponent % 2 === 1) {
            result = (result * base) % modulus;
        }

        // Right shift the exponent by 1 (equivalent to exponent //= 2)
        exponent = Math.floor(exponent / 2);
        // Square the base
        base = (base * base) % modulus;
    }

    return result;
}