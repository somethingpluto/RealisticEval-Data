#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <vector>

// Define the decryption function
std::vector<int> perform_polynomial_decryption(int degree, int modulus, const std::vector<int>& key, const std::vector<int>& encrypted_data) {
    std::vector<int> decrypted_data(degree);

    for (int index = 0; index < degree; ++index) {
        int decrypted_value = (encrypted_data[index] - key[index]) % modulus;
        if (decrypted_value < 0) {
            decrypted_value += modulus;
        }
        decrypted_data[index] = decrypted_value;
    }

    return decrypted_data;
}

TEST_CASE("Test perform_polynomial_decryption basic functionality", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(4, 5, {1, 2, 3, 4}, {5, 6, 7, 8}) == std::vector<int>{4, 4, 4, 4});
}

TEST_CASE("Test perform_polynomial_decryption with zero secret key", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(3, 7, {0, 0, 0}, {6, 13, 20}) == std::vector<int>{6, 6, 6});
}

TEST_CASE("Test perform_polynomial_decryption with zero ciphertext", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(3, 9, {1, 2, 3}, {0, 0, 0}) == std::vector<int>{8, 7, 6});
}

TEST_CASE("Test perform_polynomial_decryption with large values", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(2, 1000, {500, 500}, {1000, 1000}) == std::vector<int>{500, 500});
}