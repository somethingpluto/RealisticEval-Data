/**
 * @brief Converts temperature from log10(K) to keV for a given input.
 *
 * This function takes a temperature value in log10(K) and converts it to 
 * the equivalent temperature in keV. The input can be either a scalar 
 * (single temperature) or a tuple of temperatures.
 *
 * @param T_log10_K The temperature in log10(K). Can be a scalar (float) or a tuple of temperatures.
 * @type T_log10_K float or tuple
 *
 * @return The temperature(s) in keV corresponding to the input.
 * @rtype float or tuple
 *
 * @throws std::invalid_argument If the input is not a scalar (int or float) or a tuple.
 */

template<typename T>
auto convert_log10_K_to_keV(T T_log10_K) -> decltype(std::declval<T>() * k_B_over_keV) {}