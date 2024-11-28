#include <Eigen/Dense>
#include <iostream>

// Function to check XOR sums of specific columns in a given combination matrix.
bool check_xor_sum(const Eigen::ArrayXi& combination) {
    // Ensure that combination is an array of integers (Eigen handles this internally).

    // Calculate XOR sums for specified columns
    Eigen::ArrayXi xor_sum_0_3_6 = (combination.col(0) ^ combination.col(3) ^ combination.col(6)).eval();
    Eigen::ArrayXi xor_sum_1_4_7 = (combination.col(1) ^ combination.col(4) ^ combination.col(7)).eval();
    Eigen::ArrayXi xor_sum_2_5 = (combination.col(2) ^ combination.col(5)).eval();

    // Check if the XOR sums match the expected values
    bool all_match = true;
    all_match &= (xor_sum_0_3_6 == 0x6b).all();
    all_match &= (xor_sum_1_4_7 == 0x76).all();
    all_match &= (xor_sum_2_5 == 0x12).all();

    return all_match;
}