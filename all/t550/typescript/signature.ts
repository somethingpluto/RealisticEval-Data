const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from log10(K) to keV for a given input (number or array).
 *
 * @param T_log10_K - The temperature in log10(K). Can be a number or an array of temperatures.
 * @returns The temperature(s) in keV corresponding to the input.
 * @throws {Error} If the input is not a number or an array.
 */
function convertLog10KToKeV(T_log10_K: number | number[]): number | number[] {}