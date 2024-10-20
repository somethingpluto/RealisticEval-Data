TEST_CASE("TestCheckXorSum", "[check_xor_sum]") {
    SECTION("test_correct_xor_sums") {
        // Test with combination values that produce the expected XOR sums.
        Eigen::ArrayXi combination(2, 8);
        combination << 0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00,
                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00;
        REQUIRE_FALSE(check_xor_sum(combination));
    }

    SECTION("test_incorrect_xor_sums") {
        // Test with combination values that do not meet the expected XOR sums.
        Eigen::ArrayXi combination(2, 8);
        combination << 0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00,
                       0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00;
        REQUIRE_FALSE(check_xor_sum(combination));
    }

    SECTION("test_edge_case_with_zero") {
        // Test with a combination where all values are zero.
        Eigen::ArrayXi combination(1, 8);
        combination.setZero();
        REQUIRE_FALSE(check_xor_sum(combination));
    }

    SECTION("test_large_numbers") {
        // Test with large numbers in the combination.
        Eigen::ArrayXi combination(2, 8);
        combination << 0x6b000000, 0x00000000, 0x00000012, 0x00000000, 0x76000000, 0x00000000, 0x00000000, 0x00000000,
                       0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000;
        REQUIRE_FALSE(check_xor_sum(combination));
    }

    SECTION("test_multiple_rows") {
        // Test with a combination that contains multiple rows.
        Eigen::ArrayXi combination(3, 8);
        combination << 0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00,
                       0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00,
                       0x6b, 0x00, 0x12, 0x00, 0x76, 0x00, 0x00, 0x00;
        REQUIRE(check_xor_sum(combination));
    }
}