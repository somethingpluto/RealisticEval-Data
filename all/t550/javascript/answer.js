const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from log10(K) to keV for a given input (scalar or array).
 *
 * @param {number | number[]} T_log10_K - The temperature in log10(K). Can be a scalar or an array of temperatures.
 * @returns {number | number[]} The temperature(s) in keV corresponding to the input.
 * @throws {Error} If the input is not a scalar (number) or an array.
 */
function convertLog10KToKeV(T_log10_K) {
    // Check if the input is a scalar (number)
    if (typeof T_log10_K === 'number') {
        const T_kelvin = Math.pow(10, T_log10_K); // Convert log10(K) to K
        return T_kelvin * k_B_over_keV; // Convert K to keV
    }

    // Check if the input is an array
    if (Array.isArray(T_log10_K)) {
        return T_log10_K.map(t => Math.pow(10, t) * k_B_over_keV); // Convert each value
    }

    // Raise an error for unsupported input types
    throw new Error("Input must be a scalar (number) or an array of temperatures.");
}