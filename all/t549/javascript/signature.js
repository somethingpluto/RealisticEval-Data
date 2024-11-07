const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from keV to log10(K) for a given input (scalar or array).
 *
 * @param {number | number[]} T_keV - The temperature in keV. Can be a scalar or an array of temperatures.
 * @returns {number | number[]} The temperature(s) in log10(K) corresponding to the input.
 * @throws {Error} If the input is not a scalar (number) or an array.
 */
function getTInLog10Kelvin(T_keV) {}