#include <iostream>
#include <vector>
#include <climits> // For INT_MAX

// Function to perform polynomial decryption
std::vector<int> perform_polynomial_decryption(int degree, int modulus, const std::vector<int>& key, const std::vector<int>& encrypted_data) {
    // Decrypts the polynomial based encryption by reversing the encryption steps
    std::vector<int> decrypted_data;

    for (int index = 0; index < degree; ++index) {
        // Calculate the decrypted value considering positive modulus range
        int decrypted_value = (encrypted_data[index] - key[index]) % modulus;

        // Adjust for C++'s behavior with negative numbers
        if (decrypted_value < 0) {
            decrypted_value += modulus;
        }

        decrypted_data.push_back(decrypted_value);
    }

    return decrypted_data;
}

// Function to check the correctness of the decryption function
void check_decryption() {
    std::vector<int> key = {1, 2, 3};
    std::vector<int> encrypted_data = {5, 7, 9};
    int degree = 3;
    int modulus = 10;

    std::vector<int> decrypted_data = perform_polynomial_decryption(degree, modulus, key, encrypted_data);

    // Expected decrypted data: [4, 5, 6]
    for (int val : decrypted_data) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}