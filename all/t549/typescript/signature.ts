import { log10 } from "mathjs";

// Define the constant for conversion: Boltzmann constant in keV/K
const k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

/**
 * Converts temperature from keV to log10(K) for a given input (scalar or tuple).
 * 
 * @param T_keV - The temperature in keV. Can be a scalar or a tuple of temperatures.
 * @returns The temperature(s) in log10(K) corresponding to the input.
 * @throws {Error} If the input is not a scalar (number) or a tuple of temperatures.
 */
function getTInLog10Kelvin(T_keV: number | [number]): number | [number] {