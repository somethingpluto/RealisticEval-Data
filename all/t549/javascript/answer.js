const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

function getTInLog10Kelvin(T_keV) {
    /**
     * Converts temperature from keV to log10(K) for a given input (scalar or array).
     *
     * @param {number | number[]} T_keV - The temperature in keV. Can be a scalar or an array of temperatures.
     * @returns {number | number[]} The temperature(s) in log10(K) corresponding to the input.
     * @throws {Error} If the input is not a scalar (number) or an array.
     */

    // Check if the input is a scalar (number)
    if (typeof T_keV === 'number') {
        // Calculate log10(K) for the scalar value
        return Math.log10(T_keV / k_B_over_keV);
    }

    // Check if the input is an array
    else if (Array.isArray(T_keV)) {
        // Calculate log10(K) for each element in the array
        return T_keV.map(t => Math.log10(t / k_B_over_keV));
    }

    // Raise an error for unsupported input types
    else {
        throw new Error("Input must be a scalar (number) or an array of temperatures.");
    }
}