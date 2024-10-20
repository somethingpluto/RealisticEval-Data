// Define the constant for conversion: Boltzmann constant in keV/K
const double k_B_over_keV = 8.617333262145e-5; // eV/K to keV/K

template<typename T>
constexpr bool is_scalar(const T&) {
    return std::is_same<T, int>::value || std::is_same<T, float>::value || std::is_same<T, double>::value;
}