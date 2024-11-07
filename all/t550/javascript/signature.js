const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from log10(K) to keV for a given input (scalar or array).
 *
 * @param {number | number[]} T_log10_K - The temperature in log10(K). Can be a scalar or an array of temperatures.
 * @returns {number | number[]} The temperature(s) in keV corresponding to the input.
 * @throws {Error} If the input is not a scalar (number) or an array.
 */
function convertLog10KToKeV(T_log10_K) {}