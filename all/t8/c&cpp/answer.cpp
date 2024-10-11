#include <vector>

std::vector<int> perform_polynomial_decryption(int degree, int modulus, const std::vector<int>& key, const std::vector<int>& encrypted_data) {
    // Container for the decrypted data
    std::vector<int> decrypted_data(degree);

    for (int index = 0; index < degree; ++index) {
        // Calculate the decrypted value considering positive modulus range
        int decrypted_value = (encrypted_data[index] - key[index]) % modulus;
        
        // Adjust for negative modulus result
        if(decrypted_value < 0) {
            decrypted_value += modulus;
        }
        
        decrypted_data[index] = decrypted_value;
    }

    return decrypted_data;
}