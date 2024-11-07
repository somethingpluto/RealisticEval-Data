import { log10 } from "mathjs";

// Define the constant for conversion: Boltzmann constant in keV/K
const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

function getTInLog10Kelvin(T_keV: number | [number]): number | [number] {
    /**
     * Converts temperature from keV to log10(K) for a given input (scalar or tuple).
     *
     * @param T_keV - The temperature in keV. Can be a scalar or a tuple of temperatures.
     * @returns The temperature(s) in log10(K) corresponding to the input.
     * @throws {Error} If the input is not a scalar (number) or a tuple of temperatures.
     */

    // Check if the input is a scalar (number)
    if (typeof T_keV === 'number') {
        // Calculate log10(K) for the scalar value
        return log10(T_keV / k_B_over_keV);
    }

    // Check if the input is a tuple
    else if (Array.isArray(T_keV) && T_keV.length > 0 && T_keV.every(t => typeof t === 'number')) {
        // Calculate log10(K) for each element in the tuple
        return T_keV.map(t => log10(t / k_B_over_keV)) as [number];
    }

    // Raise an error for unsupported input types
    else {
        throw new Error("Input must be a scalar (number) or a tuple of temperatures.");
    }
}