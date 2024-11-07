const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from log10(K) to keV for a given input (number or array).
 *
 * @param T_log10_K - The temperature in log10(K). Can be a number or an array of temperatures.
 * @returns The temperature(s) in keV corresponding to the input.
 * @throws {Error} If the input is not a number or an array.
 */
function convertLog10KToKeV(T_log10_K: number | number[]): number | number[] {
    // Check if the input is a number
    if (typeof T_log10_K === 'number') {
        const T_kelvin = Math.pow(10, T_log10_K); // Convert log10(K) to K
        return T_kelvin * k_B_over_keV; // Convert K to keV
    }

    // Check if the input is an array
    else if (Array.isArray(T_log10_K)) {
        return T_log10_K.map(t => Math.pow(10, t) * k_B_over_keV); // Convert each value
    }

    // Raise an error for unsupported input types
    else {
        throw new Error('Input must be a number or an array of temperatures.');
    }
}